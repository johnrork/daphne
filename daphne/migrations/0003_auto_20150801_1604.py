# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0002_auto_20150801_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='page',
        ),
        migrations.RemoveField(
            model_name='textimagesection',
            name='section',
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textimagesection',
            name='page',
            field=models.ForeignKey(default=1, to='daphne.Page'),
            preserve_default=False,
        ),
    ]
