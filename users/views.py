from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from users import forms


class LoginView(View):
    """
        Вьюшка для отображения формы LOGIN.
        Работаем с формой LoginForm, логиним пользователя  м
        в случае успешной проверки пользователя и пароля
    """

    def get(self, request):
        form = forms.LoginForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'users/login.html', {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get("password")
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect(reverse('core:home'))
        return render(request, 'users/login.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))
