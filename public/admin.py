#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Valder Gallo on 2012-01-29.
Copyright (c) 2012 valdergallo. All rights reserved.
"""

from django.contrib import admin
from models import Tag, Public, DefaultImage, PublicImage, Comment
from sorl.thumbnail.admin import AdminImageMixin

class Admin(admin.ModelAdmin):
    pass
    
    
class TagAdmin(admin.ModelAdmin):
    pass
    
    
class PublicAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Public, PublicAdmin)
admin.site.register(DefaultImage)
admin.site.register(PublicImage)
admin.site.register(Comment)
