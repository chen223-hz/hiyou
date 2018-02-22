# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0021_point_geshu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='ba',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='geshu',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
