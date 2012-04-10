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
from django.views.generic.list_detail import object_detail

from forms import PublicForm
from public.models import Public


def public_add(request):
    public_form = PublicForm(request.POST or None)

    if request.method == 'POST':
        if public_form.is_valid():
            instance = public_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic registred with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "public/public_form.html",
                  {'public_form': public_form},
                  )


def public_update(request, public_id):
    public = get_object_or_404(Public, id=public_id)
    public_form = PublicForm(request.POST or None, instance=public)

    if request.method == 'POST':
        if public_form.is_valid():
            instance = public_form.save(commit=False)
            instance.user = request.user
            instance.save()
            instance.tags.register(request.POST['tags'])

            messages.success(request, 'Puuublic updated with success')
            return redirect(reverse('website:home_user', args=[request.user]))

    return render(request,
                  "public/public_form.html",
                  {'public_form': public_form},
                  )


def public_detail(request, public_id, public_slug):
    public = get_object_or_404(Public, id=public_id)

    return render(request,
                  "public/public_detail.html",
                  {'public': public},
                  )
