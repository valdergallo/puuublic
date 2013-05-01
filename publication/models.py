#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.conf import settings
from django.template.defaultfilters import slugify
from core.models import DefaultFields, DefaultGeoFields
from publication.managers import PublicationManager, CommentManager
from website.templatetags.default_image import random_image
from taggit.managers import TaggableManager


class Favorites(DefaultGeoFields):
    user = models.ForeignKey(User)
    theme = models.ForeignKey('Theme')
    __unicode__ = lambda self: u'{} favoritou {}'.format(self.user, self.theme)

class Theme(DefaultGeoFields):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    #url = models.SlugField(max_length=30, null=True, blank=True, db_index=True)

    def __unicode__(self):
        return self.title.title()

    def url(self):
        return "{}{}".format(settings.SITE_URL,self.get_absolute_url())


    @models.permalink
    def get_absolute_url(self):
        return ('website:theme_page',(),{
            'theme_slug': self.slug
        })

class Publication(DefaultGeoFields):
    "This is messages from one Publication"
    theme = models.ForeignKey(Theme, related_name='publications', \
        verbose_name=u"Tema",help_text=u"(selecione o tema da sua publicação)")
    user = models.ForeignKey(User, related_name='publications_set')
    title = models.CharField(max_length=255,verbose_name=u"Título")
    message = models.TextField(verbose_name=u"Mensagem")
    slug = models.SlugField(max_length=200)
    image = models.ImageField(verbose_name=u"Imagem da Publicação",upload_to='publication/%Y/%m/%d', null=True, blank=True)
    tags = TaggableManager(verbose_name=u"Tags da Publicação",help_text=u"(separe por vírgulas)",blank=True)
    published = models.BooleanField(default=True)

    #replicate count
    rated_count = models.IntegerField(default=0)
    watched_count = models.IntegerField(default=0)
    liked_count = models.IntegerField(default=0)

    objects = PublicationManager()

    class Meta:
        get_latest_by = ('-created_at',)

    def __unicode__(self):
        return self.title

    def image_default(self):
        return random_image()


    def url(self):
        return "{}{}".format(settings.SITE_URL,self.get_absolute_url())

    @models.permalink
    def get_absolute_url(self):
        return ('website:publication_detail', (), {
                'theme_slug': self.theme.slug ,
                'publication_slug': self.slug or 'pub',
            })



#publication signal
@receiver(pre_save, sender=Publication)
def check_slug(sender, instance, **kwargs):
    try:
        obj = Publication.objects.get(pk=instance.pk)
    except Publication.DoesNotExist:
        pass
    else:
        if not obj.slug == slugify(instance.title):
            nslug = slugify(instance.title)
            c = 0
            while Publication.objects.filter(theme=obj.theme,slug=nslug).count() > 0:
                c += 1
                nslug = '%s-%d'%(nslug, c)
            instance.slug = nslug



class PublicationImage(DefaultFields):
    message = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Publication/%Y/%m/%d')
    user = models.ForeignKey(User, related_name='images_set')
    publication = models.ForeignKey(Publication, related_name='publication_images_set')

    def __unicode__(self):
        return self.description


class Comment(DefaultGeoFields):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    publication = models.ForeignKey(Publication, related_name='comments_set')

    objects = CommentManager()

    def __unicode__(self):
        return self.message
