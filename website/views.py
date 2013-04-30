#!/usr/bin/python
# encoding: utf-8
"""
views.py

Desenvolvido pelo time do Puuublic.
Todos os direitos reservados.
"""
import json

from django.contrib.auth.forms import authenticate
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView

from publication.forms import SearchForm
from friendship.forms import RegisterForm, LoginForm, RecoverPassForm,\
    EditUserForm,EditProfileForm
from publication.models import Publication
from website.models import Blog
from website.forms import ContactForm

import hashlib

def home(request):
    "Starting page without login"

    if request.user.is_authenticated():
        return redirect(reverse('website:dashboard'))
    last_publication_list = Publication.objects.all().order_by('-created_at')[0:20]

    register_form = RegisterForm()
    login_form = LoginForm(request.POST or None)

    return render(request, "base.html", {
                    "page": "home",
                     "login_form": login_form,
                     "register_form": register_form,
                     "last_publication_list": last_publication_list,
                     }
                  )

@login_required
def welcome(request):
    if not request.GET.get('first'):
        return redirect('website:dashboard')
    return render(request, 'website/welcome.html')


def ajax_signup(request):
    errors = []
    if not request.is_ajax():
        return HttpResponse(':)')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password')
            #autentica usuario e redireciona via js
            new_user = authenticate(username=user.email,
                                    password=password)
            if new_user:
                print login(request, new_user)
            return HttpResponse(json.dumps({
                    'status': True,
                    'errors': []
                }), mimetype="application/json")
        else:
            msg = "Erro no cadastro"
            errors = form.errors
        return HttpResponse(
                json.dumps({
                    'status': False,
                    'msg': msg,
                    'errors': errors
                }), mimetype="application/json")
    return HttpResponse(':)')


def ajax_recover(request):
    status = False
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            status = True
        except User.DoesNotExist:
            msg = u"Usuário não existe."
            return HttpResponse(json.dumps({'status':status,'msg':msg}))

        #gera token envia email de recuperacao
        url = settings.SITE_URL + reverse('website:recover_pass',
                 kwargs={
                    'user_id': user.id,
                    'token_dev': hashlib.md5(user.email).hexdigest()
                }
            )

        email_msg = u"""
            Olá, você solicitou uma mudança de senha. Para alterá-la clique no
            link: %s
            """ % url

        sent = send_mail('[Puuublic] Recupere sua senha', email_msg,
        settings.NO_REPLY_EMAIL,[email] )
        if sent:
            status = True
            msg = u"Link de recuperacao de senha foi enviado a sua caixa de entrada."
        return HttpResponse(json.dumps({'status': status, 'msg': msg}))


def recover(request, user_id, token_dev):
    """
    Alterar senha
    """
    user = get_object_or_404(User,pk=int(user_id))
    if hashlib.md5(user.email).hexdigest() != token_dev:
        return redirect('/')

    if request.method == "POST":
        form = RecoverPassForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password1'])
            user.save()
            msg = u"Sua senha foi alterada com sucesso"
            return render(request,"website/success.html",
                {'msg':msg, }
            )
    else:
        form = RecoverPassForm()

    return render(request,"website/recover.html",
        {'form':form, }
    )



def publications(request):
    "List all publications"
    search = request.GET.get('search', '')
    _filter = request.GET.get('filter', '')
    page = request.REQUEST.get('page', 1)

    result = []
    if search:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            result = search_form.get_result_queryset()

    pub_last_update = Publication.objects.all().order_by('-created_at')[0:20]

    return render(request,
                  "website/publications.html",
                    {
                    "search": search,
                    "filter": _filter,
                    "pub_last_update": pub_last_update,
                    "page": page,
                    'result':result
                     }
                  )


def dashboard(request):
    "Following list"
    if not request.user.is_authenticated():
        return redirect(reverse('website:home'))

    get_user = request.user
    favs = get_user.favorites_set.exclude(theme__slug='descubra-o-puuublic')
    if not favs:
        pub_last_update = Publication.objects.all().order_by('-created_at')[0:20]
    else:
        themes = [i.theme for i in get_user.favorites_set.all()]
        pub_last_update = Publication.objects.filter(theme__in=themes).order_by('-created_at')[:20]
    return render(request,
                  "website/publications.html",
                    {
                    "pub_last_update": pub_last_update,
                    "get_user": get_user,
                     }
                  )


def publications_user(request, user_id):
    """
    Inicio 1
    """
    if user_id.isdigit():
        get_user = get_object_or_404(User, pk=int(user_id))
    else:
        get_user = get_object_or_404(User, userprofile__nickname=user_id)

    pub_list = get_user.publications_set.all().order_by('-rated_count', '-created_at')

    return render(request,"website/publications_user.html",
                    {
                    "get_user": get_user,
                    "pub_list":pub_list,
                     }
                  )


@login_required
def acc_config(request):

    "Configurar dados da conta"
    profile = request.user.get_profile()
    if request.method == 'POST':
        acc_config_form = EditProfileForm(request.POST, request.FILES,
                                          instance=profile,prefix="profile")
        edit_user_form = EditUserForm(request.POST, instance=request.user,
                                      prefix="user")
        if acc_config_form.is_valid() and edit_user_form.is_valid():
            user = edit_user_form.save()
            instance = acc_config_form.save(commit=False)
            instance.user = user
            instance.save()
            return redirect(user.get_profile().get_absolute_url())
    else:
        acc_config_form = EditProfileForm(instance=profile, prefix="profile")
        edit_user_form = EditUserForm(instance=request.user, prefix="user")

    return render(request, "website/acc_config.html",
      {
        "acc_config_form": acc_config_form,
        "edit_user_form": edit_user_form
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
            try:
                form.save()
            except ValueError,e:
                return HttpResponse(json.dumps({'status':True,'msg':
                    'Erro no envio do e-mail'}))
            #reset form
            form = ContactForm()
            sent = u"Sua mensagem foi enviada com sucesso"
            sent += u"<br/> Responderemos o mais rápido possível"
            sent += u"<br/> Obrigado pelo contato"
            return HttpResponse(json.dumps({'status':True,'msg':sent}))
        else:
            errors = form.errors
            print errors
            return HttpResponse(json.dumps({'status':False,'errors':errors}))
    return render(request,
                    "website/contact.html",
                    {'form': form}
                )


def ajax_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponse(json.dumps({'msg': u'Logado', 'status': True}))

    return HttpResponse(json.dumps({'msg': u'Usuário inválido', 'status': False}))


def weblogout(request):
    logout(request)
    return redirect('/')



def error_page(request):
    """
    404
    """
    last_publication_list = Publication.objects.all().order_by('-created_at')[0:20]
    return render(request,"404.html",
                    {'last_publications': last_publication_list}
                )


class EmailView(TemplateView):
    template_name = 'email.html'
    def get_context_data(self, **kwargs):
        context = super(EmailView, self).get_context_data(**kwargs)
        context['email'] = 'ellisonleao@gmail.com'
        context['password'] = 'cabeca1985'

        return context
