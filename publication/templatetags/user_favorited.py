# -*- encoding:utf-8 -*-
from django import template
from publication.models import Favorites, Theme
register = template.Library()

@register.filter("hasfavorite")
def hasfavorite(value, theme):
    theme = Theme.objects.get(pk=theme)
    try:
        Favorites.objects.get(theme=theme, user=value)
    except Favorites.DoesNotExist:
        return False
    return True
