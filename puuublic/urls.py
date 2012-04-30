from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('website.urls', app_name='website', namespace='website')),
    url(r'^accounts/login/', 'website.views.home'),
#    url(r'^accounts/', include('registration.urls')),
    url(r'^publication/', include('publication.urls', app_name='publication', namespace='publication')),
    url(r'^public_admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^public_admin/', include(admin.site.urls)),
    url(r'^public_admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
