from django import forms
from .model import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'date_joined', 'genre', 'image', 'roles', 'about')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'genre', 'image', 'roles', 'about')