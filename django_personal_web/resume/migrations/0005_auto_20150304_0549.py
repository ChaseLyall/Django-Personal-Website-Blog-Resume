# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('proficiency', models.CharField(max_length=200, choices=[(b'Novice', b'Novice'), (b'Proficient', b'Proficient'), (b'Advanced', b'Advanced'), (b'Expert', b'Expert')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(to='resume.Skill_Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.CharField(max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='employer_title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
