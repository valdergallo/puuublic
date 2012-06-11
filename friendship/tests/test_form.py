#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django_dynamic_fixture import G
from friendship.forms import LoginForm, RegisterForm
from django.core import mail


class TestForm(TestCase):

    def setUp(self):
        user = G(User, username='test', is_superuser=True, is_staff=True)
        user.set_password('test')
        user.save()

    def test_form_login(self):
        """
        Test user loged
        """
        data = {'username': 'test', 'password': 'test'}
        form = LoginForm(data)
        self.assertTrue(form.is_valid())

    def test_form_login_desactived(self):
        """
        Test user loged desactived
        """
        user = User.objects.get(username='test')
        user.is_active = False
        user.save()

        data = {'username': 'test', 'password': 'test'}
        form = LoginForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue('__all__' in form.errors)

    def test_form_login_errors(self):
        """
        Test user loged
        """
        data = {'password': 'test'}
        form = LoginForm(data)
        self.assertFalse(form.is_valid())

        self.assertTrue('username' in form.errors)

        data = {'username': 'test'}
        form = LoginForm(data)
        self.assertFalse(form.is_valid())

        self.assertTrue('password' in form.errors)

    def test_form_registration(self):
        """
        Test user registration
        """
        data = {
        'username': 'username_test',
        'password': 'password_test',
        'first_name': 'first_name_test',
        'last_name': 'last_name_test',
        'email': 'email_test'
        }

        form = RegisterForm(data)
        self.assertFalse(form.is_valid())  # invalid e-mail
        self.assertTrue('email' in form.errors)

    def test_form_registration_and_create_user(self):
        """
        Test user registration
        """
        data = {
        'username': 'username_test',
        'password': 'password_test',
        'first_name': 'first_name_test',
        'last_name': 'last_name_test',
        'email': 'email@test.com'
        }

        data['email'] = 'email@test.com'
        form = RegisterForm(data)
        self.assertTrue(form.is_valid())
        form.save()

        users = User.objects.exclude(username='test')
        self.assertEquals(users.count(), 1)

    def test_form_registration_and_create_user_send_one_email(self):
        """
        Test user registration
        """
        data = {
        'username': 'username_test',
        'password': 'password_test',
        'first_name': 'first_name_test',
        'last_name': 'last_name_test',
        'email': 'email@test.com'
        }

        data['email'] = 'email@test.com'
        form = RegisterForm(data)
        self.assertTrue(form.is_valid())
        form.save()

        users = User.objects.exclude(username='test')
        self.assertEquals(users.count(), 1)
        self.assertFalse(users[0].is_active)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, '[pubblic:contact] Email de ativação de conta - Puuublic')
