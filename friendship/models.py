# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from core.models import DefaultFields, DefaultActiveFields


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Private(models.Model):
    group = models.ForeignKey(Group, related_name='private_group')
    can_see = models.BooleanField(default=True)

class FriendshipType(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


class Friendship(DefaultActiveFields):
    owner = models.ForeignKey(User, related_name='owner')
    friend = models.ForeignKey(User, related_name='friend')
    group = models.ForeignKey(Group, related_name='group')
    fiendship_type = models.ForeignKey(FriendshipType, related_name='type')
    
    def __unicode__(self):
        return self.owner


class Follow(DefaultActiveFields):
    owner = models.ForeignKey(User, related_name='follow_owner')
    friend = models.ForeignKey(User, related_name='follow_friend')
    
    def __unicode__(self):
        return self.owner


class UserProfile(DefaultFields):
    "Extending User with DefaultFields"
    user = models.OneToOneField(User)
    url = models.URLField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    newsletter = models.BooleanField(default=True)
    date_bourn = models.DateField(null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    token_dev = models.CharField(max_length=255, null=True, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    "Signal to auto create user"
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
