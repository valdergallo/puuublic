# encoding: utf-8
from django.contrib.syndication.views import Feed
from publication.models import Publication
from django.utils.feedgenerator import Atom1Feed

class RssSiteNewsFeed(Feed):
    title = "Puuublic - Novas Publicações"
    link = "/"
    description = u"Novas Publicações atualizadas diaramente"

    def items(self):
        return Publication.objects.order_by('-created_at')[:20]

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description
