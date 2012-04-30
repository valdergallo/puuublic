#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.contrib import admin
from models import Tag, Publication, PublicationImage, Comment
from sorl.thumbnail.admin import AdminImageMixin

class Admin(admin.ModelAdmin):
    pass
    
    
class TagAdmin(admin.ModelAdmin):
    pass
    
    
class PublicationAdmin(admin.ModelAdmin):
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)
    
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationImage)
admin.site.register(Comment)
