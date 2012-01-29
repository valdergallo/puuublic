from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('public.views',
    url(r'^add/$', 'public_add', name='add'),
)
