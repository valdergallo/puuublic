#!/usr/bin/env python
# encoding: utf-8
"""
manager.py

Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.test import TestCase
from publication.models import Publication, Theme
from django.contrib.auth.models import User
from django_dynamic_fixture import G
from publication.forms import SearchForm


class PublicationManagerTest(TestCase):
    def setUp(self):
        G(Publication, n=20)
        G(Theme, n=20)
        G(User, n=20)

        publication = Publication.objects.all().order_by('?')[0]
        publication.title = 'test'
        publication.save()

        theme = Theme.objects.all().order_by('?')[0]
        theme.title = 'test'
        theme.save()

        user = User.objects.all().order_by('?')[0]
        user.username = 'test'
        user.save()

    def test_search_publication(self):
        data = {
            'filter': 'publication',
            'search': 'test'
        }
        form = SearchForm(data)

        self.assertTrue(form.is_valid())
        self.assertTrue(form.get_result_queryset().count(), 1)
        self.assertTrue(isinstance(form.get_result_queryset()[0], Publication))

    def test_search_puuublic(self):
        data = {
            'filter': 'puuublic',
            'search': 'test'
        }
        form = SearchForm(data)

        self.assertTrue(form.is_valid())
        self.assertTrue(form.get_result_queryset().count(), 1)
        self.assertTrue(isinstance(form.get_result_queryset()[0], Theme))

    def test_search_people(self):
        data = {
            'filter': 'people',
            'search': 'test'
        }
        form = SearchForm(data)

        self.assertTrue(form.is_valid())
        self.assertTrue(form.get_result_queryset().count(), 1)
        self.assertTrue(isinstance(form.get_result_queryset()[0], User))

    def test_search_show_all_publications(self):
        form = SearchForm()
        self.assertTrue(form.get_result_queryset().count(), 20)
