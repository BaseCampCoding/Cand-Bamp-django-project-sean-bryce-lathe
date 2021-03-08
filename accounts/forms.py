from django import forms
from .model import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['thing']

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ("thing",)