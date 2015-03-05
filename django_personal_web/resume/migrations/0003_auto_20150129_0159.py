# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20150129_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_month',
            field=models.DateField(help_text=b'If current job, please set end month equal to start month.'),
            preserve_default=True,
        ),
    ]
