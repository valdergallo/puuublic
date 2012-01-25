# encoding: utf-8
from django import forms
from django.db.models import Q
from django.template.defaultfilters import slugify
from public.models import Public
import re


class SearchForm(forms.Form):
    "Search values on public content everywere"

    search = forms.CharField(max_length=100)

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


class TagForm(forms.Form):
    "Add tags and split multiple values from one string like ,/ ... "

    tags = forms.CharField(max_length=255, null=True, blank=True)

    def clean_tags(self):
        value = self.cleaned_data['tags']
        strip_tags = re.split('; | , - /', value)
        if len(strip_tags):
            return [slugify(tag) for tag in strip_tags]
        else:
            return slugify(strip_tags)


class PublicForm(forms.ModelForm):
    "Add new Public"

    class Meta:
        model = Public
        fields = ('title', 'tie', 'message', 'image')

