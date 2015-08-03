# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daphne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextImageSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='image',
        ),
        migrations.RemoveField(
            model_name='section',
            name='text',
        ),
        migrations.AddField(
            model_name='textimagesection',
            name='section',
            field=models.ForeignKey(to='daphne.Section'),
        ),
    ]
