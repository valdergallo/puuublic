# encoding: utf-8
from django import forms
from django.db.models import Q
from public.models import Public

class SearchForm(forms.Form):
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
