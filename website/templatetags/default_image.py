#!/usr/bin/env python
# encoding: utf-8
"""
default.py

Created by Valder Gallo on 2012-02-27.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django import template
from random import choice

register = template.Library()

@register.simple_tag
def random_image():
    """
    Usage:  <img src='{% random_image %}'>
    """
    CHOICE_DEFAULT = (
        '/static/image/Avatar-Amarelo-67.png',
        '/static/image/Avatar-Azul-Claro-67.png',
        '/static/image/Avatar-Azul-Escuro-67.png',
        '/static/image/Avatar-Azul-Medio-67.png',
        '/static/image/Avatar-Roxo-67.png',
        '/static/image/Avatar-Verde-67.png',
        '/static/image/Avatar-Vermelho-67.png',
    )

    return choice(CHOICE_DEFAULT)
