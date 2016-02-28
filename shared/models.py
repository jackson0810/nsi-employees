from django.conf import settings
from django.db import models


from security.models import CustomUser
from shared.utilities import make_uuid


class CommonFields(models.Model):
    is_active = models.BooleanField(default=True)
    dt_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by')
    dt_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_by')

    class Mets:
        abstract = True


class FunctionalCapability(CommonFields):
    capability_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    title = models.CharField(max_length=250, verbose_name='title of functional capability')
    text = models.TextField(verbose_name='detail')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class TaskOrder(CommonFields):
    task_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    task_number = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents')

    class Meta:
        ordering = ['task_number']

    def __str__(self):
        return self.task_number


class NewsItem(CommonFields):
    news_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    featured = models.BooleanField(default=False, verbose_name='is this featured')
    title = models.CharField(max_length=250, verbose_name='title of news item')
    text = models.TextField(verbose_name='news detail')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ImageItem(CommonFields):
    image_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    featured = models.BooleanField(default=False, verbose_name='is this a featured image')
    title = models.CharField(max_length=250, verbose_name='title of image item')
    text = models.TextField(verbose_name='image detail')
    image = models.ImageField(upload_to='originals', null=True, blank=True)

    def __str__(self):
        return self.title
