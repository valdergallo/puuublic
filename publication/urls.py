#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('publication.views',
    url(r'^add/$', 'Publication_add', name='Publication_add'),
    url(r'^detail/(?P<Publication_id>\d+)/(?P<Publication_slug>\w+)/$', 'Publication_detail', name='Publication_detail'),
)
