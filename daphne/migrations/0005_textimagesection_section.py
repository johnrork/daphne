# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0004_auto_20150801_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='textimagesection',
            name='section',
            field=models.ForeignKey(default=1, to='daphne.Section'),
            preserve_default=False,
        ),
    ]
