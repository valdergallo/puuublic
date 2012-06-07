#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Valder Gallo on 2012-05-01.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django import forms
from website.models import Contact
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.ModelForm):
    "Register contact form and send email"
    class Meta:
        model = Contact


    def send_email(self):
        #TODO: send email default
        msg = u"""
        Date: %(date_send)s \n
        Nome: %(name)s \n
        Telefone: %(fone)s \n
        Cidade: %(city)s \n
        Mensagem: %(message)s
        """ % (self.instance.__dict__)

        send_mail('[pubblic:contact] Contact Message', msg, self.instance.email,
            settings.ADMINS, fail_silently=True)
