#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse

from forms import PublicationForm
from publication.models import Publication


def publication_add(request):
    publication_form = PublicationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if publication_form.is_valid():
            instance = publication_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic registred with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "publication/publication_form.html",
                  { 'publication_form': publication_form},
                  )


def publication_update(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    publication_form = PublicationForm(request.POST or None, request.FILES or None, 
                        instance=publication)

    if request.method == 'POST':
        if publication_form.is_valid():
            instance = publication_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic updated with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "publication/publication_form.html",
                  { 'publication_form': publication_form},
                  )


def publication_detail(request, publication_id, publication_slug):
    publication = get_object_or_404(Publication, id=publication_id)

    return render(request,
                  "publication/publication_detail.html",
                  { 'publication': publication},
                  )
