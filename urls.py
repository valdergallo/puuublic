from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^accounts/', include('registration.urls')),
    url(r'^', include('website.urls' , app_name='website', namespace='website')),
    url(r'^public/', include('public.urls' , app_name='public', namespace='public')),
    url(r'^pubblic_admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^pubblic_admin/', include(admin.site.urls)),
)
