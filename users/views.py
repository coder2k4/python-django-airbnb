from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
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
