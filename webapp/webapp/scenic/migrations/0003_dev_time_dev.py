# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0002_auto_20170309_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='time_dev',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
