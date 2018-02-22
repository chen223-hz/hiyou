# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0074_commodity_group_scenic'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity_group',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='commodity_group',
            name='grounding',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
