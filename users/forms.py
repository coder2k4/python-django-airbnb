from django import forms

from . import models


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", 'email', 'username')
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'Username'}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Name"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_ver = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password verification"}),
                                   label='Password verification')

    def clean_password_ver(self):
        # поля обрабатываются по порядку, мы не может из
        # clean_password получить дату password_ver
        password = self.cleaned_data.get('password')
        password_ver = self.cleaned_data.get('password_ver')
        if password != password_ver:
            raise forms.ValidationError('Password does not match')
        else:
            return password

    def save(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        # Create, but don't save the new author instance.
        user = super().save(commit=False)
        user.set_password(password)
        user.save()
