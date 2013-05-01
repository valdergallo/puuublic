#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django import forms
from django.contrib.auth.forms import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(\
            attrs={'placeholder':'******'}), required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email' : forms.TextInput(attrs={'placeholder': 'Email'}),
            'username' : forms.TextInput(attrs={'placeholder': u'Usuário'}),
        }

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'regiter_user',\
                'placeholder': u'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'register_password',\
                'placeholder': '******'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username, password)
        if user is None:
            raise forms.ValidationError(u'Usuário inválido')
            if user.is_active:
                raise forms.ValidationError(u'Usuário desativado')

    class Meta:
        model = User
        fields = ('username', 'password',)
