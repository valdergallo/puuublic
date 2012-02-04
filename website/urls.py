#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^u/(?P<username>\w+)/$', 'home_user', name='home_user'),
    url(r'^ajax_login/$', 'ajax_login', name='ajax_login'),
    url(r'^logout/$', 'weblogout', name='weblogout'),
    url(r'^novidades/$', 'novidades', name='novidades'),
    url(r'^institucional/$', 'institucional' , name='institucional'),
    url(r'^termos/$', 'termos', name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
)
