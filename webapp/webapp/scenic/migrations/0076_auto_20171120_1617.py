# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0075_auto_20171120_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='price_old',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='price',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
