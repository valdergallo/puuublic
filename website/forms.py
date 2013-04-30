#!/usr/bin/env python
# encoding: utf-8
from django import forms
from website.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.localflavor.br.forms import BRPhoneNumberField


class ContactForm(forms.ModelForm):
    "Register contact form and send email"

    name = forms.CharField(error_messages={'required':u'Nome é campo obrigatório'})
    email = forms.EmailField(error_messages={'required':u'Email é campo obrigatório'})

    fone = BRPhoneNumberField(help_text=u"Ex: 99-9999-9999",required=False,\
        error_messages={'invalid':u'Informe um número no formato XX-XXXX-XXXX'})

    message = forms.CharField(widget=forms.Textarea,error_messages={
        'required':u"Digite uma mensagem"
    })

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

        sent = send_mail('[Puuublic] Contato ', msg,
        settings.NO_REPLY_EMAIL,[self.instance.email] )
        return True if sent == 1 else False

    def save(self, *args, **kwargs):
        self.send_email()
        super(ContactForm, self).save(*args, **kwargs)
