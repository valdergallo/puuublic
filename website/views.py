# encoding: utf-8
from django.shortcuts import render
from public.models import Public
from friendship.forms import RegisterForm, LoginForm
from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect


def home(request, page=1):
    "Starting page without login"
    must_popular_public_list = Public.objects.must_popular(page=page)
    last_public_list = Public.objects.lastest_five()

    register_form = RegisterForm()
    login_form = LoginForm()

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


def weblogin(request):
    if request.method == 'POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        if user.is_active:
        login(request, user)
        # success
        return HttpResponseRedirect('/')
    else:
        # disabled account
        return render(request, 'inactive_account.html')
    else:
        # invalid login
        return render(request, 'invalid_login.html')

def weblogout(request):
    logout(request)
    return render(request, 'logged_out.html')
