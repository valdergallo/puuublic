# encoding: utf-8
from django.db import models
from core.models import DefaultFields


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name


class BlogManager(models.Manager):
    
    def lastest_five(self):
        try:
            return Blog.objects.acitives().order_by('-date_created')[0:5]
        except Blog.DoesNotExist:
            return Public.objects.none()

    def acitives(self):
        return super(BlogManager, self).get_query_set().filter(active=1)
        
    def canceleds(self):
        return super(BlogManager, self).get_query_set().filter(active=0)


class Blog(DefaultFields):
    title = models.CharField(max_length=255)
    tie = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='public/%Y/%m/%d')
    category = models.ManyToManyField(Category)
    
    objects = BlogManager()
    
    def __unicode__(self):
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
            return ('blog', (), {
                'slug': self.slug,
            })



