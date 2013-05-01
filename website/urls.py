#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^recuperar/(?P<user_id>\d+)/(?P<token_dev>\w+)/$', 'recover', name='recover_pass'),
    url(r'^publicacoes/$', 'publications', name='publications'),
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'^ajax_login/$', 'ajax_login', name='ajax_login'),
    url(r'^ajax_signup/$', 'ajax_signup', name='ajax_signup'),
    url(r'^ajax_recover/$', 'ajax_recover', name='ajax_recover'),
    url(r'^logout/$', 'weblogout', name='weblogout'),
    url(r'^institucional/$', 'institucional', name='institucional'),
    url(r'^termos/$', 'termos', name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
    url(r'^conta/$', 'acc_config', name='acc_config'),
    url(r'^bem-vindo/$', 'welcome', name='welcome'),
    url(r'^perfil/(?P<user_id>\w+)/$', 'publications_user', name='publications_user'),
)

urlpatterns += patterns('publication.views',
    url(r'^ajax_add_favorite/$', 'ajax_add_favorite', name='ajax_add_favorite'),
    url(r'^puuublic/adicionar/$', 'publication_add', name='publication_add'),
    url(r'^puuublic/tema/adicionar/$', 'theme_add', name='theme_add'),
    url(r'^publicacao/puuublic/buscar/json/$', 'ajax_theme_search', name='ajax_theme_search'),
    url(r'^(?P<theme_slug>[\w-]+)/(?P<publication_slug>[\w-]+)/editar/$', 'edit_publication', name='edit_publication'),
    url(r'^(?P<theme_slug>[\w-]+)/(?P<publication_slug>[\w-]+)/$', 'publication_detail', name='publication_detail'),
    url(r'^(?P<theme_slug>[\w-]+)/$', 'theme_page', name='theme_page'),
)
