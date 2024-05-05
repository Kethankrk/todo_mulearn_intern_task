from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Todo
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.utils import timezone


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'eg: name@gmail.com'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'enter same password'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': "Enter username"}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': "Enter password"}))


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'expire']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'expire': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
    
    