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
from public.managers import TagManager, DefaltImageManager, PublicManager, CommentManager


class Liked(DefaultFields):
    user = models.ForeignKey(User, related_name='user_liked')
    public = models.ForeignKey('Public', related_name='public_liked')


class Foward(DefaultFields):
    user = models.ForeignKey(User, related_name='user_foward')
    public = models.ForeignKey('Public', related_name='public_foward')


class Watched(DefaultFields):
    user = models.ForeignKey(User, related_name='user_watched')
    public = models.ForeignKey('Public', related_name='public_watched')


class Rated(DefaultFields):
    user = models.ForeignKey(User, related_name='user_rated')
    public = models.ForeignKey('Public', related_name='public_rated')


class Alert(DefaultFields):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='user_alert')
    public = models.ForeignKey('Public', related_name='public_alert')

    def __unicode__(self):
        return self.message


class Tag(DefaultFields):
    value = models.CharField(max_length=100)

    def __unicode__(self):
        return self.value


class PublicTag(DefaultFields):
    tag = models.ForeignKey(Tag)
    public = models.ForeignKey('Public', related_name='tags')

    objects = TagManager()

    def __unicode__(self):
        return self.tag.value


class Public(DefaultGeoFields):
    "This is messages from one public"
    user = models.ForeignKey(User, related_name='publics')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parents')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='public/%Y/%m/%d', null=True, blank=True)

    #replicate count
    rated_count = models.IntegerField(default=0)
    watched_count = models.IntegerField(default=0)
    liked_count = models.IntegerField(default=0)

    objects = PublicManager()

    class Meta:
        get_latest_by = ('date_created',)

    def __unicode__(self):
        return self.title

    def default(self):
        return DefaultImage.objects.random()

    @models.permalink
    def get_absolute_url(self):
        return ('public:public_detail', (), {
                'public_slug': self.slug or 'pub',
                'public_id': self.id,
            })


class DefaultImage(DefaultFields):
    image = models.ImageField(upload_to='default/%Y/%m/%d')

    objects = DefaltImageManager()

    def __unicode__(self):
        return self.image.name


class PublicImage(DefaultFields):
    message = models.CharField(max_length=250)
    image = models.ImageField(upload_to='public/%Y/%m/%d')
    user = models.ForeignKey(User, related_name='images')
    public = models.ForeignKey(Public, related_name='public_images')

    def __unicode__(self):
        return self.description


class Comment(DefaultGeoFields):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    public = models.ForeignKey(Public, related_name='comments')

    objects = CommentManager()

    def __unicode__(self):
        return self.message


class PublicPermission(DefaultFields):
    owner = models.ForeignKey(User, related_name='permission_user')
    friend = models.ForeignKey(User, related_name='permission_friend')
    public = models.ForeignKey(Public, related_name='permission_public')
