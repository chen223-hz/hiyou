# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0060_auto_20171009_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='census',
            name='other',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
