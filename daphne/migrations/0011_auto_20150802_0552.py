# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0010_section_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section_id',
            new_name='related_id',
        ),
        migrations.RemoveField(
            model_name='gallerysection',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='section',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='textimagesection',
            name='uuid',
        ),
    ]
