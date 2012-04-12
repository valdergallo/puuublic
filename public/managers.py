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


class TagManager(ActiveManager):

    def register(self, values):
        from public.models import Public, PublicTag

        tags = list(set(re.split(',| |-|/|\"|\'', values)))  # split value
        tags = [x for x in tags if x]  # clear empty values
        for tag in tags:
            tag, _ = self.get_or_create(value=slugify(tags))
            public = Public.objects.get(id=self.core_filters.get('public__id'))
            PublicTag.objects.get_or_create(tag=tag, public=public)
        return tags


class PublicManager(ActiveManager):

    def must_popular(self, page=1, limit=10):
        query = self.all().order_by('-rated_count')
        paginator = Paginator(query, limit)
        query_list = paginator.page(page)
        return query_list.object_list

    def lastest_five(self):
        return self.all().order_by('-date_created')[0:5]


class DefaltImageManager(models.Manager):

    def random(self):
        if not cache.get('query_cache'):
            cache.set('query_cache', self.objects.all())

        query_cache = cache.get('query_cache')

        if query_cache.exists():
            return query_cache.order_by('?')[0]
        else:
            return None


class CommentManager(ActiveManager):

    def last_ten(self, page=1, limit=10):
        query = self.objects.all().order_by('-date_created')
        paginator = Paginator(query, limit)
        query_list = paginator.page(page)
        return query_list.object_list
