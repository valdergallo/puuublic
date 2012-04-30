#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('publication.views',
    url(r'^add/$', 'publication_add', name='publication_add'),
    url(r'^detail/(?P<publication_id>\d+)/(?P<publication_slug>\w+)/$', 'publication_detail', name='publication_detail'),
)
