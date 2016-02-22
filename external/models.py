from django.conf import settings
from django.db import models


from security.models import CustomUser


class FunctionalCapability(models.Model):
    title = models.CharField(max_length=250, verbose_name='title of functional capability')
    text = models.TextField(verbose_name='detail')
    dt_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='func_created_by')
    dt_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='func_updated_by')

    def __str__(self):
        return self.title


class NewsItem(models.Model):
    featured = models.BooleanField(default=False, verbose_name='is this featured')
    title = models.CharField(max_length=250, verbose_name='title of news item')
    text = models.TextField(verbose_name='news detail')
    dt_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by')
    dt_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_by')

    def __str__(self):
        return self.title


class ImageItem(models.Model):
    featured = models.BooleanField(default=False, verbose_name='is this a featured image')
    title = models.CharField(max_length=250, verbose_name='title of image item')
    text = models.TextField(verbose_name='image detail')
    image = models.ImageField(upload_to='originals', null=True, blank=True)
    dt_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created_by')
    dt_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_updated_by')

    def __str__(self):
        return self.title
