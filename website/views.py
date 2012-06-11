#!/usr/bin/python
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
from django.core.mail import send_mail

from publication.forms import SearchForm
from friendship.forms import RegisterForm, LoginForm
from publication.models import Publication
from website.models import Blog
from website.forms import ContactForm


def home(request):
    "Starting page without login"
    page = request.REQUEST.get('page', 1)

    if request.user.is_authenticated():
        return redirect(reverse('website:dashboard', args=[request.user]))

    must_popular_publication_list = Publication.objects.must_popular(page=page)
    last_publication_list = Publication.objects.lastest_five()

    register_form = RegisterForm()
    login_form = LoginForm(request.POST or None)
    search_form = SearchForm(request.POST or None)

    return render(request,
                  "website/home.html",
                    {
                    "search_form": search_form,
                     "login_form": login_form,
                     "register_form": register_form,
                     "must_popular_publication_list": must_popular_publication_list,
                     "last_publication_list": last_publication_list,
                     }
                  )

def ajax_signup(request):
    p = {}
    errors = []
    status = False
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.create_user():
                status = True
                msg = u"Enviamos um email para %s" % form.cleaned_data['email']
                msg += u" com as instruções para ativação da sua conta."
                msg += u" Por favor confira sua caixa de entrada"
            else:
                status = False
                msg += u"Erro ao enviar o e-mail"
        else:
            errors = form.errors
            msg = u"Erro no Cadastro, favor corrigir"

        return HttpResponse(json.dumps({'status':status,'msg':msg,'errors':errors}),mimetype="application/json")


def activate_user(request,user_id,token):
    """
    Verifica e ativa o user
    """
    user = get_object_or_404(User,pk=int(user_id))
    profile = user.get_profile()

    if token == profile.token:
        if user.is_active:
            msg = u"Usuário já ativado"
        else:
            user.is_active = True
            user.save()
            msg = u"Usuário Ativado. Faça o login com seu usuário e senha"
    else:
        msg = u"Erro na ativação"

    return render(request,"website/success.html",
        {'msg':msg, }
    )



def publications(request):
    "List all publications"
    search = request.GET.get('search', '')
    _filter = request.GET.get('filter', '')
    page = request.REQUEST.get('page', 1)

    search_form = SearchForm(request.GET or None)

    if search:
        if search_form.is_valid():
            pub_list = search_form.get_result_queryset()
    else:
        pub_list = Publication.objects.all().order_by('-rated_count', '-updated_at')

    pub_last_update = Publication.objects.all().order_by('-updated_at')[0:10]

    return render(request,
                  "website/publications.html",
                    {
                    "search": search,
                    "filter": _filter,
                    "search_form": search_form,
                    "pub_list": pub_list,
                    "pub_last_update": pub_last_update,
                    "page": page
                     }
                  )


def dashboard(request, username):
    "Following list"
    search = request.POST.get('search', '')
    page = request.REQUEST.get('page', 1)
    get_user = get_object_or_404(User, username=username)

    search_form = SearchForm(request.POST or None)

    if request.method == 'POST':
        if search_form.is_valid():
            pub_list = search_form.get_result_queryset()
    else:
        pub_list = Publication.objects.filter(user__in=get_user.following.all()).order_by('-rated_count', '-updated_at')

    pub_last_update = pub_list.order_by('-updated_at')[0:10]

    return render(request,
                  "website/publications.html",
                    {
                    "search": search,
                    "search_form": search_form,
                    "pub_list": pub_list,
                    "pub_last_update": pub_last_update,
                    "page": page
                     }
                  )


def publications_user(request, username):
    "Starting page with login"
    search = request.POST.get('search', '')
    get_user = get_object_or_404(User, username=username)

    search_form = SearchForm(request.POST or None)

    if request.method == 'POST':
        if search_form.is_valid():
            pub_list = search_form.get_result_queryset()
    else:
        pub_list = get_user.publications_set.all().order_by('-rated_count', '-updated_at')

    return render(request,
                  "website/publications_user.html",
                    {
                    "get_user": get_user,
                    "search": search,
                    "search_form": search_form,
                    "pub_list": pub_list,
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
                    "search_form": search_form,
                    }
                )


def contato(request):
    "Contato without login"

    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form.send_email()
            #reset form
            form = ContactForm()
            sent = u"Sua mensagem foi enviada com sucesso"
            sent += u"<br/> Responderemos o mais rápido possível"
            sent += u"<br/> Obrigado pelo contato"
            return HttpResponse(json.dumps({'status':True,'msg':sent}))
        else:
            error = u"Erro no envio. Cheque os dados"
            return HttpResponse(json.dumps({'status':False,'msg':error}))
    return render(request,
                    "website/contact.html",
                    {'form': form}
                )


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
