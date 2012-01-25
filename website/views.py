# encoding: utf-8
import json

from django.contrib.auth.forms import authenticate
from django.contrib.auth.views import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from public.forms import SearchForm
from friendship.forms import RegisterForm, LoginForm
from public.models import Public


def home(request, page=1):
    "Starting page without login"
    must_popular_public_list = Public.objects.must_popular(page=page)
    last_public_list = Public.objects.lastest_five()

    register_form = RegisterForm()
    login_form = LoginForm()
    search_form = SearchForm()

    if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			return redirect('/')

    return render(request,
                  "website/home.html",
                    {
                     "login_form":login_form,
                     "register_form":register_form,
                     "must_popular_public_list":must_popular_public_list,
                     "last_public_list":last_public_list,
                     }
                  )


def novidades(request):
    "News without login"
    return render(request, "base.html")


def institucional(request):
    "Institucional without login"
    return render(request, "base.html")


def termos(request):
    "Termo without login"
    return render(request, "base.html")


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
