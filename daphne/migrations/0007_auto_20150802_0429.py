# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0006_gallerysection'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='classes',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
