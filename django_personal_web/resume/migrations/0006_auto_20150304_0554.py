# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20150304_0549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill_category',
            old_name='name',
            new_name='category_name',
        ),
    ]
