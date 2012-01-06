# encoding: utf-8
from django.db import models
from core.models import DefaultFields, DefaultActiveFields
from django.contrib.auth.models import User
import re


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


class Tag(DefaultActiveFields):
    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tag


class PublicTag(models.Model):
    tag = models.ForeignKey(Tag)
    public = models.ForeignKey('Public')

    @staticmethod
    def add(self, value, public):
        tags = list(set(re.split(',| |-' , value)))
        for tag in tags:
            if tag:
                tag, _ = Tag.objects.get_or_create(tag)
                pubtag, _ = PublicTag.objects.get_or_create(tag, public)
                return pubtag
            else:
                return None

    def __unicode__(self):
        return self.tag


class Public(DefaultFields):
    user = models.ForeignKey(User, related_name='users')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parents')
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='public/%Y/%m/%d')
    rated_count = models.IntegerField(default=0)
    rated = models.ForeignKey(Rated, null=True, blank=True, related_name='rated')
    watched_count = models.IntegerField(default=0)
    watched = models.ForeignKey(Watched, null=True, blank=True, related_name='watched')
    liked_count = models.IntegerField(default=0)
    liked = models.ForeignKey(Liked, null=True, blank=True, related_name='liked')

    def __unicode__(self):
        return self.title


class PublicImage(DefaultActiveFields):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    public = models.ForeignKey(Public)


class Comment(DefaultActiveFields):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    public = models.ForeignKey(Public)


class PublicPermission(DefaultActiveFields):
    owner = models.ForeignKey(User, related_name='permission_user')
    friend = models.ForeignKey(User, related_name='permission_friend')
    public = models.ForeignKey(Public, related_name='permission_public')
