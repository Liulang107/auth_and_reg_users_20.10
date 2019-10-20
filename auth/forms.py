from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput)
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля:', widget=forms.PasswordInput)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput)
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput)
