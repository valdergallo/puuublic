#!/usr/bin/env python
# encoding: utf-8
"""
default.py

Created by Valder Gallo on 2012-02-27.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django import template
from django.conf import settings
from public.models import DefaultImage

register = template.Library()

@register.simple_tag
def random_image():
    """
    Usage:  <img src='{% random_image %}'>
    """
    return DefaultImage.objects.random().image.url