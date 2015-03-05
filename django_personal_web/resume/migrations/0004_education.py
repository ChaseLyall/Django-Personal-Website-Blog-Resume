# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20150129_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=200)),
                ('concentration', models.CharField(max_length=200)),
                ('gpa', models.CharField(max_length=200)),
                ('graduation_month', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
