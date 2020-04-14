from django.shortcuts import render

# Create your views here.
from django.views import View
from users import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'users/login.html', {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'users/login.html', {"form": form})
