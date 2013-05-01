#!/usr/bin/env python
# encoding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail

from captcha.models import CaptchaStore

from friendship.forms import LoginForm, RegisterForm

class TestForm(TestCase):

    fixtures = ['captcha.json']
    
    def setUp(self):
        captcha = CaptchaStore.objects.get(pk=1)
        self.post = {
            'password1': u'password1',
            'password2': u'password1',
            'email1': u'email1@email.com',
            'email2': u'email1@email.com',
            'captcha_0': captcha.hashkey,
            'captcha_1': captcha.response,
        }

    def test_form_login(self):
        """
        Test user loged
        """
        data = {'username': 'test@test.com', 'password': 'test'}
        form = LoginForm(data)
        self.assertTrue(form.is_valid())

    def test_form_registration(self):
        """
        Test user registration
        """
        form = RegisterForm(self.post)
        print form.errors
        self.assertTrue(form.is_valid())
