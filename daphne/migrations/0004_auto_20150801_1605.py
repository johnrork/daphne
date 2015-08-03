# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0003_auto_20150801_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textimagesection',
            name='page',
        ),
        migrations.AddField(
            model_name='section',
            name='page',
            field=models.ForeignKey(default=1, to='daphne.Page'),
            preserve_default=False,
        ),
    ]
