#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

import re

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import models
from django.template.defaultfilters import slugify


from core.models import DefaultFields, DefaultActiveFields


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


class TagManager(models.Manager):
    
    def register(self,values):
        tags = list(set(re.split(',| |-|/|\"|\'', values))) #split value
        tags = [x for x in tags if x] #clear empty values
        for tag in tags:
            tag, _ = Tag.objects.get_or_create(tag=slugify(tags))
            public = Public.objects.get(id=self.core_filters.get('public__id'))
            pubtag, _ = PublicTag.objects.get_or_create(tag=tag, public=public)
             
        return tags
    

class Tag(DefaultActiveFields):
    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tag


class PublicTag(models.Model):
    tag = models.ForeignKey(Tag)
    public = models.ForeignKey('Public', related_name='tags')
    
    objects = TagManager()
 
    def __unicode__(self):
        return self.tag.tag


class PublicManager(models.Manager):

    def must_popular(self, page=1, limit=10):
        query = Public.objects.acitives().order_by('-rated_count')
        paginator = Paginator(query, limit)
        query_list = paginator.page(page)
        return query_list.object_list

    def lastest_five(self):
        try:
            return Public.objects.acitives().order_by('-date_created')[0:5]
        except Public.DoesNotExist:
            return Public.objects.none()

    def acitives(self):
        return super(PublicManager, self).get_query_set().filter(active=1)
        
    def canceleds(self):
        return super(PublicManager, self).get_query_set().filter(active=0)


class Group(DefaultFields):
    "This is one Puuublic"
    user = models.ForeignKey(User, related_name='public_groups')
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='group/%Y/%m/%d')
    
    class Meta:
        get_latest_by = ('date_created',)

    def __unicode__(self):
        return self.title 
        
    @models.permalink
    def get_absolute_url(self):
        return ('public', (), {
            'slug': self.slug,
        })


class Public(DefaultFields):
    "This is messages from one public"
    user = models.ForeignKey(User, related_name='publics')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parents')
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='public/%Y/%m/%d')
    
    group = models.ForeignKey(Group)
    
    #replicate count
    rated_count = models.IntegerField(default=0)
    watched_count = models.IntegerField(default=0)
    liked_count = models.IntegerField(default=0)
      
    objects = PublicManager()

    class Meta:
        get_latest_by = ('date_created',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('public', (), {
            'group': self.group,
            'slug': self.slug,
        })


class PublicImage(DefaultActiveFields):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='images')
    public = models.ForeignKey(Public)


class Comment(DefaultActiveFields):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='comments')
    public = models.ForeignKey(Public)


class PublicPermission(DefaultActiveFields):
    owner = models.ForeignKey(User, related_name='permission_user')
    friend = models.ForeignKey(User, related_name='permission_friend')
    public = models.ForeignKey(Public, related_name='permission_public')
