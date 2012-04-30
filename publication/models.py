#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.contrib.auth.models import User
from django.db import models

from core.models import DefaultFields, DefaultGeoFields
from publication.managers import TagManager, PublicationManager, CommentManager
from website.templatetags.default_image import random_image


class Liked(DefaultFields):
    user = models.ForeignKey(User, related_name='user_liked')
    Publication = models.ForeignKey('Publication', related_name='publication_liked')


class Foward(DefaultFields):
    user = models.ForeignKey(User, related_name='user_foward')
    Publication = models.ForeignKey('Publication', related_name='publication_foward')


class Watched(DefaultFields):
    user = models.ForeignKey(User, related_name='user_watched')
    Publication = models.ForeignKey('Publication', related_name='publication_watched')


class Rated(DefaultFields):
    user = models.ForeignKey(User, related_name='user_rated')
    Publication = models.ForeignKey('Publication', related_name='publication_rated')


class Alert(DefaultFields):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='user_alert')
    Publication = models.ForeignKey('Publication', related_name='publication_alert')

    def __unicode__(self):
        return self.message


class Tag(DefaultFields):
    value = models.CharField(max_length=100)

    def __unicode__(self):
        return self.value


class PublicationTag(DefaultFields):
    tag = models.ForeignKey(Tag)
    Publication = models.ForeignKey('Publication', related_name='tags')

    objects = TagManager()

    def __unicode__(self):
        return self.tag.value


class Publication(DefaultGeoFields):
    "This is messages from one Publication"
    user = models.ForeignKey(User, related_name='publications')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parents')
    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=30, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='publication/%Y/%m/%d', null=True, blank=True)

    #replicate count
    rated_count = models.IntegerField(default=0)
    watched_count = models.IntegerField(default=0)
    liked_count = models.IntegerField(default=0)

    objects = PublicationManager()

    class Meta:
        get_latest_by = ('date_created',)

    def __unicode__(self):
        return self.title

    def default(self):
        return random_image()

    @models.permalink
    def get_absolute_url(self):
        return ('publication:publication_detail', (), {
                'publication_slug': self.slug or 'pub',
                'publication_id': self.id,
            })


class PublicationImage(DefaultFields):
    message = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Publication/%Y/%m/%d')
    user = models.ForeignKey(User, related_name='images')
    Publication = models.ForeignKey(Publication, related_name='publication_images')

    def __unicode__(self):
        return self.description


class Comment(DefaultGeoFields):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    Publication = models.ForeignKey(Publication, related_name='comments')

    objects = CommentManager()

    def __unicode__(self):
        return self.message


class PublicationPermission(DefaultFields):
    owner = models.ForeignKey(User, related_name='permission_user')
    friend = models.ForeignKey(User, related_name='permission_friend')
    Publication = models.ForeignKey(Publication, related_name='permission_Publication')
