# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0033_point_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facilities',
            name='scenic_facilities',
        ),
    ]
