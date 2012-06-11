#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(\
            attrs={'placeholder': '******'}), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        user_exists = User.objects.filter(Q(username = username) \
                | Q(email = email))

        if user_exists:
            raise forms.ValidationError(u'Usuário já existe')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': u'Usuário'}),
        }

    def create_user(self):
        """
        Cria o usuário
        """
        if not self.cleaned_data:
            self.is_valid()

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.set_password(password)
        user.is_active = False
        user.save()
        profile = user.get_profile()
        link = reverse('activate_user', args=[user.id, profile.token])
        msg = u"""
        Link para ativação: %(link)s
        """ % link

        return send_mail('[pubblic:contact] Email de ativação de conta - Puuublic',
            msg,
            user.email,
            'ellisonleao@gmail.com')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'regiter_user',\
                'placeholder': u'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'register_password',\
                'placeholder': '******'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError(u'Usuário inválido')
        if not user.is_active:
            raise forms.ValidationError(u'Usuário desativado')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password',)
