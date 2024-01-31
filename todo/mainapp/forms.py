from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Task

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={ }))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description','deadline')