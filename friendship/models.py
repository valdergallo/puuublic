#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.core.urlresolvers import reverse

from core.models import DefaultFields

class UserProfile(DefaultFields):
    "Extending User with DefaultFields"
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to="profile/%Y/%m/%d",
                              blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    newsletter = models.BooleanField(
        verbose_name="Deseja receber newsletter com novidades?",
        blank=True,
        default=True
    )
    birthday = models.DateField(verbose_name=u"Aniversário",
                                null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name=u"País",
                               blank=True, null=True)
    city = models.CharField(max_length=200, verbose_name=u"Cidade",
                            blank=True, null=True)

    nickname = models.CharField(max_length=100, verbose_name=u'Url de Perfil',
                                blank=True, null=True)

    objects = models.Manager()


    @property
    def get_url(self):
        if self.user.get_profile().url:
            return self.url
        return self.user.get_profile().get_absolute_url()


    def get_absolute_url(self):
        if self.nickname:
            ident = self.nickname
        else:
            ident = self.user.id
        return reverse('website:publications_user', kwargs={
            'user_id': ident }
        )

    def profile_url(self):
        if self.url:
            return self.url
        return self.get_absolute_url()

def create_user_profile(sender, instance, created, **kwargs):
    "Signal to auto create user"
    if created:
        #gerar token aqui?
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
