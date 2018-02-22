# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0011_region_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='online_time',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dev',
            name='time_dev',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
