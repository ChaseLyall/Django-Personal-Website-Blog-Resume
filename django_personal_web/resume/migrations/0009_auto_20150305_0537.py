# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20150305_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
