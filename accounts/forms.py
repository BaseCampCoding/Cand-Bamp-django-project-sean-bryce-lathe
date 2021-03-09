from django import forms
from .model import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'genre', 'image', 'roles', 'about',)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'genre', 'image', 'roles', 'about',)