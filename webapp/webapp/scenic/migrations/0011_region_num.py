# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0010_scenic_probe'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
