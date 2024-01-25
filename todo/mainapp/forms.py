from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import Task

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={ }))

