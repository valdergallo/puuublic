from django.contrib.sitemaps import Sitemap

from publication.models import Publication, Theme

class PublicationSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Publication.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class ThemeSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return Theme.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()

        return Publication.objects.all().order_by('-created_at')

sitemaps = {
    'puuublics': ThemeSitemap,
    'publications': PublicationSitemap,
}
