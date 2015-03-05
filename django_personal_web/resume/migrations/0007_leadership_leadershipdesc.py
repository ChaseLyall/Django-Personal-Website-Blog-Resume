# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20150304_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_month', models.DateField()),
                ('end_month', models.DateField(help_text=b'If current job, please set end month equal to start month.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LeadershipDesc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('leadership', models.ForeignKey(to='resume.Leadership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
