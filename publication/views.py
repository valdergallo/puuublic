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
    Publication_form = PublicationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if Publication_form.is_valid():
            instance = Publication_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic registred with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "Publication/Publication_form.html",
                  {'Publication_form': Publication_form},
                  )


def publication_update(request, Publication_id):
    Publication = get_object_or_404(Publication, id=Publication_id)
    Publication_form = PublicationForm(request.POST or None, request.FILES or None, 
    instance=Publication)

    if request.method == 'POST':
        if Publication_form.is_valid():
            instance = Publication_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic updated with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "Publication/Publication_form.html",
                  {'Publication_form': Publication_form},
                  )


def publication_detail(request, Publication_id, Publication_slug):
    Publication = get_object_or_404(Publication, id=Publication_id)

    return render(request,
                  "Publication/Publication_detail.html",
                  {'Publication': Publication},
                  )
