#!/usr/bin/env python
# encoding: utf-8
"""
default.py

Created by Valder Gallo on 2012-02-27.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django import template
from public.models import DefaultImage

register = template.Library()

@register.simple_tag
def random_image():
    """
    Usage:  <img src='{% random_image %}'>
    """
    try:
        DefaultImage.objects.random().image.url
    except:
        return '/static/image/Avatar-Amarelo-67.png'
