from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^ajax_login/$', 'ajax_login', name='ajax_login'),
    url(r'^logout/$', 'weblogout', name='weblogout'),
    url(r'^novidades/$', 'novidades', name='novidades'),
    url(r'^institucional/$', 'institucional', name='institucional'),
    url(r'^termos/$', 'termos', name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
)
