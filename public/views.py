#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.shortcuts import render

from forms import PublicForm


def public_add(request):
    public_form = PublicForm(request.POST or None)
    
    if not request.method == 'POST':
        if public_form.is_valid():
            public_form.save()
            public_form.tags.add(request.POST['tags'])
    
    return render(request,
                  "website/home.html",
                  )
    
