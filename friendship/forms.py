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
from django.core.mail import send_mail


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

    def password_clean(self):
        password = self.instance.set_password(self.cleaned_data['password'])
        return password

    @staticmethod
    def send_email(user):
        """
        Cria o usuário
        """
        profile = user.get_profile()
        link = reverse('website:activate_user',
            args=[user.id, profile.token])
        msg = u"""
        Link para ativação: %(link)s
        """ % {'link': link}

        return send_mail('[pubblic:contact] Email de ativação de conta - Puuublic',
            msg,
            user.email,
            ['ellisonleao@gmail.com'])

    def save(self, *args, **kwargs):
        self.instance.is_active = False
        user = super(RegisterForm, self).save(*args, **kwargs)
        self.send_email(user)



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
