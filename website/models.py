#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.db import models
from core.models import DefaultGeoFields
from core.managers import ActiveManager, CanceledManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class BlogManager(ActiveManager):

    def lastest_five(self):
        return Blog.objects.all().order_by('-date_created')[0:5]


class Blog(DefaultGeoFields):
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='public/%Y/%m/%d')
    category = models.ManyToManyField(Category)

    objects = BlogManager()
    

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
            return ('blog', (), {
                'slug': self.slug,
            })



