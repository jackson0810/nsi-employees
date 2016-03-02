# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shared.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0013_contactitem_dt_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactitem',
            name='contact_uuid',
            field=models.CharField(max_length=36, db_index=True, default=shared.utilities.make_uuid),
        ),
    ]
