# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shared.utilities
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0008_auto_20160301_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalCapability',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('capability_uuid', models.CharField(max_length=36, db_index=True, default=shared.utilities.make_uuid)),
                ('title', models.CharField(max_length=250, verbose_name='title of functional capability')),
                ('text', models.TextField(verbose_name='detail')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('image_uuid', models.CharField(max_length=36, db_index=True, default=shared.utilities.make_uuid)),
                ('title', models.CharField(max_length=250, verbose_name='title of image item')),
                ('text', models.TextField(null=True, blank=True, verbose_name='image detail')),
                ('image', models.ImageField(upload_to='/vagrant/shared/static/img/slides')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('news_uuid', models.CharField(max_length=36, db_index=True, default=shared.utilities.make_uuid)),
                ('featured', models.BooleanField(default=False, verbose_name='is this featured')),
                ('title', models.CharField(max_length=250, verbose_name='title of news item')),
                ('text', models.TextField(verbose_name='news detail')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TaskOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('task_uuid', models.CharField(max_length=36, db_index=True, default=shared.utilities.make_uuid)),
                ('task_number', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='/vagrant/shared/static/documents')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['task_number'],
            },
        ),
    ]
