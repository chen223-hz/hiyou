# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0036_area_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='zhu',
            field=models.BooleanField(default=False),
        ),
    ]
