# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0007_auto_20150802_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerysection',
            name='uuid',
            field=models.UUIDField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textimagesection',
            name='uuid',
            field=models.UUIDField(default=1),
            preserve_default=False,
        ),
    ]
