#!/usr/bin/env python
# encoding: utf-8
"""
manager.py

Created by Valder Gallo on 2012 - 04 - 10.
Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.db import models


class BasicManager(models.Manager):
    def get_query_set(self):
        "Active by default"
        return super(BasicManager, self).get_query_set().filter(active=1)

    def canceleds(self):
        "Show canceled content"
        return super(BasicManager, self).get_query_set().filter(active=0)

