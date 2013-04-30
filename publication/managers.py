#!/usr/bin/env python
# encoding: utf-8
"""
manager.py

Copyright (c) 2012 valdergallo. All rights reserved.
"""
import re

from django.db import models
from django.core.cache import cache
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator

from core.managers import ActiveManager


class PublicationManager(ActiveManager):

    def must_popular(self, page=1, limit=10):
        query = self.all().order_by('-rated_count', '-updated_at')
        paginator = Paginator(query, limit)
        query_list = paginator.page(page)
        return query_list.object_list

    def lastest_five(self):
        return self.all().order_by('-updated_at')[0:5]
    def lastest_fifteen(self):
        return self.all().order_by('-updated_at')[0:15]


class DefaltImageManager(models.Manager):

    def random(self):
        if not cache.get('query_cache'):
            cache.set('query_cache', self.all())

        query_cache = cache.get('query_cache')

        if query_cache.exists():
            return query_cache.order_by('?')[0]
        else:
            return None


class CommentManager(ActiveManager):

    def last_ten(self, page=1, limit=10):
        query = self.all().order_by('-updated_at')
        paginator = Paginator(query, limit)
        query_list = paginator.page(page)
        return query_list.object_list
