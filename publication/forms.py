#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django import forms
from django.db.models import Q
from tinymce.widgets import TinyMCE
from publication.models import Publication


class SearchForm(forms.Form):
    "Search values on Publication content everywere"
    search = forms.CharField(max_length=100, required=False)

    def get_result_queryset(self):
        query = Q()
        if not self.cleaned_data:
            raise forms.ValidationError('Form need be clear')

        value = self.cleaned_data['search']
        query |= Q(title__icontains=value)
        query |= Q(themes__title__icontains=value)
        query |= Q(message__icontains=value)
        query |= Q(tags__tag__value__icontains=value)

        return Publication.objects.select_realted('themes').filter(query)


class PublicationForm(forms.ModelForm):
    "Add new Publication"
    url = forms.CharField(max_length=30, required=False, help_text='<br> Ex.: meupuuublic.puuublic.com')
    message = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))
    tags = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Publication
        fields = ('title', 'message', 'image', 'url')
