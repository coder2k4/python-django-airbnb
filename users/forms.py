from django import forms

from . import models


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return password
            else:
                self.add_error("password", forms.ValidationError("Password does't match"))
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does't exist")
