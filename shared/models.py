from sorl.thumbnail import ImageField, get_thumbnail

from django.conf import settings
from django.db import models


from security.models import CustomUser
from shared.utilities import make_uuid


class CommonFields(models.Model):
    is_active = models.BooleanField(default=True)
    dt_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
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
    document = models.FileField(upload_to='{}/shared/static/documents'.format(settings.SITE_ROOT))

    class Meta:
        ordering = ['task_number']

    def __str__(self):
        return self.task_number

    @property
    def get_document_name(self):
        return self.document.url.split('/')[-1]


class NewsItem(CommonFields):
    news_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    featured = models.BooleanField(default=False, verbose_name='is this featured')
    title = models.CharField(max_length=250, verbose_name='title of news item')
    text = models.TextField(verbose_name='news detail')
    news_year = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_item_year(self):
        return self.dt_updated.year


class ImageItem(CommonFields):
    image_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    title = models.CharField(max_length=250, verbose_name='title of image item')
    text = models.TextField(verbose_name='image detail', blank=True, null=True)
    featured = models.BooleanField(default=True, verbose_name='is this a featured image')
    image = models.ImageField(upload_to='{}/shared/static/img/slides'.format(settings.SITE_ROOT))

    def __str__(self):
        return self.title

    @property
    def get_image_name(self):
        return self.image.url.split('/')[-1]

    def get_thumbnail(self):
        return get_thumbnail(self.image, '555x350', quality=99)


class ContactItem(models.Model):
    contact_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=250, db_index=True)
    message = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=30)
    dt_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class FormCategory(CommonFields):
    category_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    category = models.CharField(max_length=250, verbose_name='form category', help_text='hold down command')

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category

    @property
    def get_my_forms(self):
        return self.formdata_set.all()


class FormData(CommonFields):
    form_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    title = models.CharField(max_length=250, verbose_name='title of form')
    text = models.TextField(verbose_name='form detail', blank=True, null=True)
    document = models.FileField(upload_to='{}/shared/static/forms'.format(settings.SITE_ROOT))
    category = models.ManyToManyField(FormCategory)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def get_document_name(self):
        return self.document.url.split('/')[-1] if self.document else None
