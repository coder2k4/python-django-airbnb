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
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password does't match"))
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does't exist")


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=80, required=False)
    last_name = forms.CharField(max_length=80, required=False)
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_ver = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = models.User.objects.get(username=username)
            if user is not None:
                raise forms.ValidationError('User already exists!')
        except models.User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError('User with this password already exists')
        except models.User.DoesNotExist:
            return email

    def clean_password_ver(self):
        # поля обрабатываются по порядку, мы не может из
        # clean_password получить дату password_ver
        password = self.cleaned_data.get('password')
        password_ver = self.cleaned_data.get('password_ver')
        if password != password_ver:
            raise forms.ValidationError('Password does not match')
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = models.User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
