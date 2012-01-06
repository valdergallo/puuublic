# encoding: utf-8
from django.db import models


class DefaultFields(models.Model):
    """
    Class Abstract Fields with latitude (lat), longitude (lon)
    created date (date_created), updated date (date_updated)
    and active (active)
    """
    lat = models.FloatField(null=True, blank=True, db_index=True)
    lon = models.FloatField(null=True, blank=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DefaultActiveFields(models.Model):
    """
    Class Abstract Fields with latitude (lat), longitude (lon)
    created date (date_created), updated date (date_updated)
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        abstract = True


class DefaultDateFields(models.Model):
    """
    Class Abstract Fields with latitude (lat), longitude (lon)
    created date (date_created), updated date (date_updated)
    """
    lat = models.FloatField(null=True, blank=True, db_index=True)
    lon = models.FloatField(null=True, blank=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
