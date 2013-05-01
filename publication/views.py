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
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.defaultfilters import slugify


from publication.forms import PublicationForm, ThemeForm, \
    CommentForm
from publication.models import Publication, Theme, Favorites
import simplejson

@login_required
def publication_add(request):
    if request.method == 'POST':
        publication_form = PublicationForm(request.POST, request.FILES)
        if publication_form.is_valid():
            instance = publication_form.save(user=request.user)
            instance.save()
            publication_form.save_m2m()
            url = instance.get_absolute_url()
            return redirect(url)
            #return HttpResponse(simplejson.dumps({'status':True,'url':url})) 
        """
        else:
            errors = publication_form.errors
            return HttpResponse(simplejson.dumps({'status':False,'errors':errors}))
        """
    else:
        if request.GET.get('theme',False):
            theme_name = request.GET.get('theme')
            theme = get_object_or_404(Theme,slug=theme_name)
            publication_form = PublicationForm(initial={'theme_name':theme.title,'theme_id':theme.id })
        else:
            publication_form = PublicationForm()

    return render(request,
                  "publication/publication_form.html",
                  {'publication_form': publication_form},
                  )


@login_required
def edit_publication(request, theme_slug,publication_slug):
    publication = get_object_or_404(Publication, slug=publication_slug,\
        user=request.user)
    theme = get_object_or_404(Theme,slug=theme_slug)
    if request.method == 'POST':
        publication_form = PublicationForm(request.POST,\
            request.FILES,instance=publication)
        if publication_form.is_valid():
            publication_form.save()
            publication_form.save_m2m()
            return redirect('website:publication_detail', theme_slug=theme.slug,
                publication_slug=publication.slug)

    else:
        publication_form = PublicationForm(instance=publication,\
            initial={'theme_name':theme.title})

    return render(request,"publication/publication_form.html",{
                'publication_form': publication_form,
            })


#@login_required
def publication_detail(request, theme_slug, publication_slug):
    theme = get_object_or_404(Theme,slug=theme_slug)
    publication = get_object_or_404(Publication,theme=theme,slug=publication_slug)
    comments = publication.comments_set.all() 
    
    if request.method == "POST":
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            instance = form_comment.save(commit=False)
            instance.user = request.user
            instance.publication = publication
            instance.save()
            messages.success(request, 'Comentário adicionado com sucesso')
    else:
        form_comment = CommentForm()
    print publication.user.get_profile().get_url
    return render(request,"publication/publication_detail.html",{
                      'publication': publication,
                      'form_comment':form_comment,
                      'comments':comments
                  })


#@login_required
def theme_page(request,theme_slug):
    """
    Pagina de um tema
    """
    try:
        theme = Theme.objects.get(slug__exact=theme_slug)
    except Theme.DoesNotExist:
        form = ThemeForm()
        page = request.REQUEST.get('page', 1)
        pub_list = []
        pub_last_update = Publication.objects.all().order_by('-created_at')[0:20]
        return render(request,'publication/theme_form.html',{
            'theme_slug':theme_slug,
            'theme_form': form,
            "pub_list": pub_list,
            "pub_last_update": pub_last_update,
            "page": page
        })
    #theme = get_object_or_404(Theme,slug=theme_slug)
    page = request.REQUEST.get('page', 1)
    pub_list = Publication.objects.filter(theme=theme).order_by('-created_at')[0:20]
    
    return render(request,
                  "publication/theme_page.html",
                    {
                    "theme": theme,
                    "pub_list": pub_list,
                    "page": page
                     }
                  )


@login_required
def theme_add(request):
    
    if request.method == "POST":
        theme_form = ThemeForm(request.POST)
        if theme_form.is_valid():
            slug = slugify(theme_form.cleaned_data['title']) 
            if Theme.objects.filter(slug__exact=slug).count() > 0:
                url = reverse("website:theme_page",\
                    kwargs={'theme_slug':slug})
                return HttpResponse(simplejson.dumps({'status':True,'url':url}))
            instance = theme_form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.title)
            instance.save()
            url = reverse("website:theme_page",\
                kwargs={'theme_slug':instance.slug})
            return HttpResponse(simplejson.dumps({'status':True,'url':url}))
        else:
            errors = theme_form.errors
            return HttpResponse(simplejson.dumps({'status':False,'errors':errors}))
    else:
        theme_form = ThemeForm()

    return render(request,
              "publication/theme_form.html",
              {
                'theme_form': theme_form,
                },
              )

def ajax_theme_search(request):
    """
    Retorna um json com os temas
    """

    result = {}
    result['status'] = False
    q = request.GET.get('term',None)
    if q:
        themes = Theme.objects.filter(title__icontains=q)
        """
        l_theme = []
        for t in themes:
            l_theme.append({'title': t.title, 'id': t.id})

        result['themes'] = l_theme
        result['status'] = True
        """
        theme_list = [i.title for i in themes]
    return HttpResponse(simplejson.dumps(theme_list), mimetype="application/json")


def ajax_add_favorite(request):
    if not request.is_ajax():
        return HttpResponse(':)')

    if request.method == "POST":
        theme_id = request.POST.get('key')
        theme = get_object_or_404(Theme, pk=int(theme_id))
        try:
            fav = Favorites.objects.get(user=request.user, theme=theme)
            print "achou"
            print fav
        except Favorites.DoesNotExist:
            fav = Favorites.objects.create(user=request.user, theme=theme)
            print "criou"
            print fav
            return HttpResponse(simplejson.dumps({'status': True,
                                                  'action': 'add'}),
                                mimetype="application/json")
        fav.delete()
        return HttpResponse(simplejson.dumps({'status': True,
                                              'action': 'remove'}),
                            mimetype="application/json")
    else:
        return HttpResponse(':)')
