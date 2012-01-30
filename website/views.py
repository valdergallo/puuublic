# encoding: utf-8
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

    register_form = RegisterForm()
    login_form = LoginForm()
    search_form = SearchForm()

    if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			return redirect(reverse('website:home'))

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
    user = get_object_or_404(User, username=username)
    must_popular_public_list = user.publics.must_popular(page=page)
    last_public_list = Public.objects.lastest_five()
    search_form = SearchForm()
    
    return render(request,
                  "website/home_user.html",
                    {
                    "search_form":search_form,
                     "must_popular_public_list":must_popular_public_list,
                     "last_public_list":last_public_list,
                     }
                  )
    

def novidades(request):
    "News without login"
    blog_list = Blog.objects.lastest_five()
    
    return render(request, 
                "website/novidades.html",
                    {
                    "blog_list": blog_list,
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
