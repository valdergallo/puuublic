# encoding: utf-8
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)

