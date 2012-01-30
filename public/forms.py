#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

import re

from django import forms
from django.db.models import Q
from django.template.defaultfilters import slugify

from public.models import Public


class SearchForm(forms.Form):
    "Search values on public content everywere"

    search = forms.CharField(max_length=100, required=False)

    def get_result_queryset(self):
        query = Q()
        if not self.cleaned_data:
            raise forms.ValidationError('Form no is clean')

        value = self.cleaned_data['search']
        query |= Q(title__icontains=value)
        query |= Q(tie__icontains=value)
        query |= Q(message__icontains=value)
        query |= Q(publictag__tag__icontains=value)

        return value, Public.objects.filter(query)


 
class PublicForm(forms.ModelForm):
    "Add new Public"
    tags = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Public
        fields = ('title', 'tie', 'message', 'image')

