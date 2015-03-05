# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='date_range',
        ),
        migrations.AddField(
            model_name='job',
            name='end_month',
            field=models.DateField(default=datetime.datetime(2015, 1, 29, 1, 17, 16, 374906, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='start_month',
            field=models.DateField(default=datetime.datetime(2015, 1, 29, 1, 17, 31, 307384, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='employer_title',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
