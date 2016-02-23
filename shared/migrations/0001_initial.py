# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import shared.utilities


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalCapability',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('capability_uuid', models.CharField(default=shared.utilities.make_uuid, max_length=36, db_index=True)),
                ('title', models.CharField(verbose_name='title of functional capability', max_length=250)),
                ('text', models.TextField(verbose_name='detail')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='func_created_by')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='func_updated_by')),
            ],
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('image_uuid', models.CharField(default=shared.utilities.make_uuid, max_length=36, db_index=True)),
                ('featured', models.BooleanField(verbose_name='is this a featured image', default=False)),
                ('title', models.CharField(verbose_name='title of image item', max_length=250)),
                ('text', models.TextField(verbose_name='image detail')),
                ('image', models.ImageField(blank=True, null=True, upload_to='originals')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='image_created_by')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='image_updated_by')),
            ],
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('news_uuid', models.CharField(default=shared.utilities.make_uuid, max_length=36, db_index=True)),
                ('featured', models.BooleanField(verbose_name='is this featured', default=False)),
                ('title', models.CharField(verbose_name='title of news item', max_length=250)),
                ('text', models.TextField(verbose_name='news detail')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_by')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='updated_by')),
            ],
        ),
    ]
