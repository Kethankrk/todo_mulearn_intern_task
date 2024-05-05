from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Todo
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.utils import timezone


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'expire']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'expire': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
    
    