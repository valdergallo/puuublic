from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap

from filebrowser.sites import site
admin.autodiscover()

from website.views import EmailView
from website.sitemap import sitemaps
from website.feed import RssSiteNewsFeed, AtomSiteNewsFeed
from publication.models import Publication

news = {
    'googlenews': GenericSitemap({
        'queryset': Publication.objects.order_by('-created_at'),
        'limit': 0.5,
        'changefreq': 'daily',
        'date_field': 'created_at'
    }),
}

urlpatterns = patterns('',
    url(r'^public_admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^public_admin/varnish/', include('varnishapp.urls')),
    url(r'^public_admin/', include(admin.site.urls)),
    url(r'^public_admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^email-template/?$', EmailView.as_view()),
    url(r'^sitemap-googlenews\.xml$', 'django.contrib.sitemaps.views.sitemap',
        { 'sitemaps': news , 'template_name': 'sitemap_googlenews.xml' }),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {
        'sitemaps': sitemaps,
    }),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^rss/$', RssSiteNewsFeed()),
    url(r'^atom/$', AtomSiteNewsFeed()),
    url(r'^', include('website.urls', app_name='website', namespace='website')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
