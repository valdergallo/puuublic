#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.db import models
from core.models import DefaultGeoFields
from core.managers import ActiveManager


class Contact(models.Model):
    name = models.CharField(max_length=100, help_text=u"Qual o seu nome completo?")
    city = models.CharField(blank=True, max_length=100, help_text=u"Diga-nos de onde você é")
    email = models.EmailField(help_text=u"Qual é o seu e-mail?")
    fone = models.CharField(blank=True, max_length=100, help_text=u"Qual é o seu telefone com DDD?")
    message = models.TextField(blank=True, help_text=u"Digite a mensagem")
    date_send = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class BlogManager(ActiveManager):

    def lastest_five(self):
        return self.all().order_by('-created_at')[0:5]


class Blog(DefaultGeoFields):
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='Publication/%Y/%m/%d')
    category = models.ManyToManyField(Category)

    objects = BlogManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
            return ('blog', (), {
                'slug': self.slug,
            })
