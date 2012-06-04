#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^publications/$', 'publications', name='publications'),
    url(r'^dashboard/(?P<username>\w+)/$', 'dashboard', name='dashboard'),
    url(r'^ajax_login/$', 'ajax_login', name='ajax_login'),
    url(r'^logout/$', 'weblogout', name='weblogout'),
    url(r'^novidades/$', 'novidades', name='novidades'),
    url(r'^institucional/$', 'institucional', name='institucional'),
    url(r'^termos/$', 'termos', name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
    url(r'^user/(?P<username>\w+)/$', 'publications_user', name='publications_user'),
)
