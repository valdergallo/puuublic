from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^u/(?P<username>\w+)/$', 'home_user', name='home_user'),
    url(r'^ajax_login/$', 'ajax_login', name='ajax_login'),
    url(r'^logout/$', 'weblogout', name='weblogout'),
    url(r'^novidades/$', 'novidades', name='novidades'),
    url(r'^institucional/$', direct_to_template,{'template': 'website/institucional.html'} , name='institucional'),
    url(r'^termos/$', direct_to_template , {'template': 'website/termos.html'} , name='termos'),
    url(r'^contato/$', 'contato', name='contato'),
)
