# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('external', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('featured', models.BooleanField(verbose_name='is this a featured image', default=False)),
                ('title', models.CharField(max_length=250, verbose_name='title of news item')),
                ('text', models.TextField(verbose_name='new detail')),
                ('image', models.ImageField(blank=True, upload_to='originals', null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='image_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='image_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='newsitem',
            name='text',
            field=models.TextField(verbose_name='new detail', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title of news item'),
        ),
    ]
