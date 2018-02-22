# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0023_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='area',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='area',
            name='update_time',
        ),
    ]
