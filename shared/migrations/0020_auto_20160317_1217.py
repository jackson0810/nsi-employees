# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0019_formcategory_category_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formcategory',
            options={'ordering': ['category']},
        ),
        migrations.AddField(
            model_name='formdata',
            name='data_type',
            field=models.CharField(choices=[('form', 'Form'), ('link', 'Link')], max_length=5, default='form'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formdata',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='url to website'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='/vagrant/shared/static/forms'),
        ),
    ]
