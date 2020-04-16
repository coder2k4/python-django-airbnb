import os

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.core.files.base import ContentFile
from django.shortcuts import redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, CreateView

from users import forms, models


class Login(FormView):
    """
        Login(FormView)
        Работаем с формой LoginForm, логиним пользователя
    """
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class Logout(LogoutView):
    """
    Logout(LogoutView)
    Выкидываем пользователя из авторизации
    """
    next_page = reverse_lazy("core:home")


class Sighup(FormView):
    """
        Sighup(FormView)
        Вьюшка регистрации пользователя
    """
    template_name = "users/sighup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "Nicolas", "last_name": "Serr", "email": "apex@example.com"}

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(self, key):
    """ Верификация емейла по ключу """
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_confirmed = True
        user.save()
        # todo: success message
    except models.User.DoesNotExist:
        # todo: add error message
        pass
    return redirect(reverse('core:home'))


def github_login(request):
    # ключ от нашего Github APP
    client_id = os.environ.get('GH_ID', None)
    # адрес, куда попадет пользователь на нашем сайте, после авторизации на github
    redirect_uri = "http://airbnb-live-dev.ap-northeast-2.elasticbeanstalk.com/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        # данные нашего приложения на github
        client_id = os.environ.get('GH_ID', None)
        client_secret = os.environ.get('GH_SECRET', None)
        # получаем code, после того как гитхаб редиректнет на нас пользователя
        code = request.GET.get('code', None)
        if code is not None:
            # получаем токен по запросу через код
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token_request.json()
            error = token_json.get('error', None)
            if error is not None:
                raise GithubException("Can't get access token")
            else:
                access_token = token_json.get('access_token')
                # При удачном получении токена, отправляем запрос на получение данных пользователя
                profile_request = request.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                # пробуем получить имя пользователя, если пользователя получили, заполняем поля данными
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    try:
                        # проверяем на существование пользователя в базе,
                        user = models.User.objects.get('name')
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException(f"Please log in with: {user.login_method}")
                    except models.User.DoesNotExist:
                        # если пользователя не найден, создаем пользоваетля
                        user = models.User.objects.create(
                            email=email,
                            first_name=name,
                            username=name,
                            bio=bio,
                            login_method=models.User.LOGIN_GITHUB,
                            email_verified=True,
                        )
                        # заполняем неиспользуемый пароль, и сохраняем пользователя
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException("Can't get your profile")
        else:
            raise GithubException("Can't get code")
    except GithubException as e:
        # todo message
        return redirect(reverse("users:login"))



    except GithubException:
        return redirect(reverse('users:login'))


def kakao_login(request):
    client_id = os.environ.get('KAKAO_ID', None)
    redirect_uri = "https://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}")


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get('code')
        client_id = os.environ.get('KAKAO_ID', None)
        token_request = requests.GET.get(f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code')
        token_json = token_request.json()
        error = token_json.get('error', None)
        if error is not None:
            raise KakaoException('ERROR getting token')
        access_token = token_json.get('access')
        profile_request = requests.get("https://kauth.kakao.com/oauth/...",
                                       headers={"Authorization": f"Bearer {access_token}"})
        profile_json = profile_request.json()
        email = profile_json.get("email")
        if email is None:
            raise KakaoException('Email not found')
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        thubnail_image = properties.get("profile_image")
        try:
            # проверяем на существование пользователя в базе,
            user = models.User.objects.get('nickname')
            if user.login_method != models.User.LOGING_KAKAO:
                raise KakaoException(f"Please log in with: {user.login_method}")
        except models.User.DoesNotExist:
            # если пользователя не найден, создаем пользоваетля
            user = models.User.objects.create(
                email=email,
                username=nickname,
                first_name=nickname,
                login_method=models.User.LOGING_KAKAO,
                email_verified=True,
            )
            # заполняем неиспользуемый пароль, и сохраняем пользователя
            user.set_unusable_password()
            user.save()
            if user.avatar is None:
                photo_request = requests.get(thubnail_image)  # URL линк на картинку
                user.avatar.save(f"{nickname}", ContentFile(photo_request.content))  # Закидываем из буфера в файл
        login(request, user)
        return redirect(reverse("core:home"))

    except KakaoException:
        return redirect(reverse('users:login'))
