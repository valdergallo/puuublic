#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.test import TestCase
from django.contrib.auth.models import User


class TestForm(TestCase):

    def setUp(self):
        user = User.objects.create(username='admin', is_superuser=True, is_staff=True)
        user.set_password('admin')
        user.save()

    def test_basic_addition(self):
        """
        Test user loged
        """
        self.assertEqual(1 + 1, 2)
