#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.shortcuts import render

from forms import PublicForm,RegisterPublicForm


def public_add(request):
    public_form = PublicForm(request.POST or None)
    
    if not request.method == 'POST':
        if public_form.is_valid():
            public_form.save()
            public_form.tags.add(request.POST['tags'])
    
    return render(request,
                  "public/public_form.html",
                  { 'public_form': public_form },
                  )
    
    
def group_public_add(request):
    public_form = RegisterPublicForm(request.POST or None)
    
    if not request.method == 'POST':
        if public_form.is_valid():
            public_form.save()
            public_form.tags.add(request.POST['tags'])
    
    return render(request,
                  "public/register_public_form.html",
                  { 'public_form': public_form },
                  )
    
