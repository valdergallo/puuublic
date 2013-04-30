#!/usr/bin/env python
# encoding: utf-8
"""
manager.py

Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.test import TestCase
from publication.models import Publication
from django_dynamic_fixture import G


class PublicationManagerTest(TestCase):
    def setUp(self):
        G(Publication, n=20)
        G(Publication, active=False, n=10)

    def test_active_content(self):
        active_Publication = Publication.objects.all()
        self.assertTrue(all([i.active for i in active_Publication]))
        self.assertEqual(active_Publication.count(), 20)

    def test_get_must_popular(self):
        pub = Publication.objects.must_popular()
        self.assertEqual(pub.count(), 10)

    def test_get_last_five(self):
        pub = Publication.objects.lastest_five()
        self.assertEqual(pub.count(), 5)

    def test_canceled_content(self):
        canceled_Publication = Publication.canceleds.all()
        self.assertFalse(all([i.active for i in canceled_Publication]))
        self.assertEqual(canceled_Publication.count(), 10)
