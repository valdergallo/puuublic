#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('public.views',
    url(r'^add/$', 'public_add', name='add'),
)
