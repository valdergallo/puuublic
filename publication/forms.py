#!/usr/bin/env python
# encoding: utf-8
from django.conf import settings
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from publication.models import Publication, Theme, Comment

from bs4 import BeautifulSoup
from ckeditor.widgets import CKEditorWidget

class SearchForm(forms.Form):
    "Search values on Publication content everywere"
    search = forms.CharField(max_length=100, required=False,\
        widget=forms.TextInput(attrs={'placeholder':'Busque aqui..',\
            'class':'search-large'} ))

    def get_result_queryset(self):
        query = Q()
        value = self.data.get('search', '')
        #_filter = self.data.get('filter', 'publication')

        #if _filter == 'publication':
        query |= Q(title__icontains=value)
        query |= Q(theme__title__icontains=value)
        query |= Q(message__icontains=value)
        query |= Q(tags__name__icontains=value)
        publications =  Publication.objects.select_related('themes').filter(query).order_by('-created_at')
        query = Q()

        #if _filter == 'puuublic':
        query |= Q(title__icontains=value)
        themes =  Theme.objects.filter(query)
        
        query = Q()
        #if _filter == 'people':
        query |= Q(first_name__icontains=value)
        query |= Q(last_name__icontains=value)
        query |= Q(username__icontains=value)

        people = User.objects.filter(query)

        count = publications.count() + themes.count() + people.count()
        return {
            'publications':publications,
            'people':people,
            'themes':themes,
            'count':count
        }


class PublicationForm(forms.ModelForm):
    "Add new Publication"
    theme_name = forms.CharField(label=u"Nome do Puuublic",max_length=50,\
        required=True,widget=forms.TextInput(attrs={'class':'theme-large'}),\
        error_messages={
            'required':u'Escolha um puuublic',
        })

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'theme-large'}),\
        error_messages={
            'required':u'Escolha um Título'
        })

    message = forms.CharField(widget=CKEditorWidget(attrs={'cols': 80, 'rows': 30}),
            error_messages={'required':u'Digite uma mensagem'}
        )


    class Meta:
        model = Publication
        fields = ('theme_name','title', 'message', 'image')

    def clean_message(self):
        message = self.cleaned_data.get('message')
        #links externos adicionando _blank
        soup = BeautifulSoup(message)
        for link in soup.findAll('a'):
            link.attrs['target'] = '_blank'
        return unicode(soup)


    def clean_theme_name(self):
        title = self.cleaned_data['theme_name']
        try:
            Theme.objects.get(title=title)
        except Theme.DoesNotExist:
            raise forms.ValidationError(u'Tema Inválido')

        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(u'Tamanho limite da imagem: 3MB')
        return image


    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        theme = Theme.objects.get(title=self.cleaned_data['theme_name'])
        instance =  super(PublicationForm, self).save(commit=False)
        if not instance.slug:
            nslug = slugify(self.cleaned_data['title'])
            c = 0
            while Publication.objects.filter(theme=theme,slug=nslug).count() > 0:
                c += 1
                nslug = '%s-%d'%(nslug, c)
            instance.slug = nslug
        if user:
            instance.user = user
        if theme:
            instance.theme = theme
        instance.save()
        return instance



class ThemeForm(forms.ModelForm):
    "Create a new puublic"
    title = forms.CharField(max_length=50, required=True,\
        widget=forms.TextInput(attrs={\
            'class':'theme-large',
        }))

    def clean_title(self):
        title = self.cleaned_data['title']
        placeholder = u'Digite o nome do novo puuublic (Máximo 50 caracteres)'
        if title == '' or title == placeholder:
            raise forms.ValidationError(u'Digite um título')

        return title

    class Meta:
        model = Theme
        fields = ('title',)

class CommentForm(forms.ModelForm):
   
    message = forms.CharField(label=u"Mensagem",max_length=200,widget=forms.TextInput(attrs={
            'class':'theme-large',
        }))
 
    class Meta:
        model = Comment
        fields = ('message',)
