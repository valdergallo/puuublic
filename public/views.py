#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from forms import PublicForm


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
                  { 'public_form': public_form },
                  )