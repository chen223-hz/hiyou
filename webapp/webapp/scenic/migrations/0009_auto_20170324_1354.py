# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0008_auto_20170322_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='dev',
        ),
        migrations.AddField(
            model_name='visitor',
            name='isdel',
            field=models.BooleanField(default=False),
        ),
    ]
