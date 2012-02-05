#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

import json

from django.contrib.auth.forms import authenticate
from django.contrib.auth.views import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from public.forms import SearchForm
from friendship.forms import RegisterForm, LoginForm
from public.models import Public
from website.models import Blog
  

def home(request):
    "Starting page without login"
    page = request.REQUEST.get('page', 1)
    
    if request.user.is_authenticated():
        return redirect(reverse('website:home_user', args=[request.user]))
       
    must_popular_public_list = Public.objects.must_popular(page=page)
    last_public_list = Public.objects.lastest_five()

    register_form = RegisterForm(request.POST or None)
    login_form = LoginForm(request.POST or None)
    search_form = SearchForm(request.POST or None)
 

    return render(request,
                  "website/home.html",
                    {
                    "search_form":search_form,
                     "login_form":login_form,
                     "register_form":register_form,
                     "must_popular_public_list":must_popular_public_list,
                     "last_public_list":last_public_list,
                     }
                  )


@login_required
def home_user(request, username):
    "Starting page with login"
    page = request.REQUEST.get('page', 1)
    search = request.POST.get('search', '')
    user = get_object_or_404(User, username=username)
    
    pub_list = user.publics.must_popular(page=page)
    search_form = SearchForm(request.POST or None)
    
    if request.method == 'POST':
        if search_form.is_valid():
            pub_list = search_form.get_result_queryset()
    
    return render(request,
                  "website/home_user.html",
                    {
                    "search": search,
                    "search_form": search_form,
                    "pub_list": pub_list
                     }
                  )
    

 
def institucional(request):
    "Institucional without login"
    search_form = SearchForm(request.POST or None)
    return render(request, "website/institucional.html", {'search_form': search_form})


def termos(request):
    "Termo without login"
    search_form = SearchForm(request.POST or None)
    return render(request, "website/termos.html", {'search_form': search_form})



def novidades(request):
    "News without login"
    search_form = SearchForm(request.POST or None)
    blog_list = Blog.objects.lastest_five()
    
    return render(request, 
                "website/novidades.html",
                    {
                    "blog_list": blog_list,
                    "search_form":search_form,
                    }
                )
 
 
def contato(request):
    "Contato without login"
    return render(request, "base.html")


def ajax_login(request):
    if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps({'msg': u'Logado', 'status': True}))
			return HttpResponse(json.dumps({'msg': u'Usuário desativado', 'status': False}))

    return HttpResponse(json.dumps({'msg': u'Usuário inválido', 'status': False}))


def weblogout(request):
    logout(request)
    return redirect('/')
