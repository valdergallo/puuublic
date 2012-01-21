# encoding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import authenticate

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'regiter_user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'register_password'}))

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

