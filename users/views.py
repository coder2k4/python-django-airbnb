from pprint import pprint

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.http import request
from django.shortcuts import redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView

from users import forms


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
    next_page = reverse_lazy("core:home")
