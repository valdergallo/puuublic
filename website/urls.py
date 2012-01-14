from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^novidades/$', 'novidades', name='novidades'),
    url(r'^institucional/$', 'institucional', name='institucional'),
    url(r'^termos/$', 'termos', name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
)
