#!/usr/bin/env python
# encoding: utf-8
"""
manager.py

Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.test import TestCase
from public.models import Public
from django_dynamic_fixture import G


class PublicManagerTest(TestCase):
    def setUp(self):
      G(Public,parent=None, n=20)
      G(Public,parent=None,active=False, n=10)

    def test_active_content(self):
        active_public = Public.objects.all()
        self.assertTrue(all([i.active for i in active_public]))
        self.assertEqual(active_public.count(), 20)

    def test_get_must_popular(self):
        pub = Public.objects.must_popular()
        self.assertEqual(pub.count(), 10)

    def test_get_last_five(self):
        pub = Public.objects.lastest_five()
        self.assertEqual(pub.count(), 5)

    def test_canceled_content(self):
        canceled_public = Public.canceleds.all()
        self.assertFalse(all([i.active for i in canceled_public]))
        self.assertEqual(canceled_public.count(), 10)
