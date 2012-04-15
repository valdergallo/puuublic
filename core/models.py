#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.db import models
from core.managers import CanceledManager


class DefaultFields(models.Model):
    """
    Class Abstract Fields with latitude (lat), longitude (lon)
    created date (date_created), updated date (date_updated)
    and active (active)
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, db_index=True)
    
    objects = models.Manager()
    canceleds = CanceledManager()
    
    class Meta:
        abstract = True


class DefaultGeoFields(DefaultFields):
    """
    Class Abstract Fields with created date (date_created),
    updated date (date_updated) and active
    """
    lat = models.FloatField(null=True, blank=True, db_index=True)
    lon = models.FloatField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
