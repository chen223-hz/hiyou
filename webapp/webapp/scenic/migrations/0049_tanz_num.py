# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0048_auto_20170816_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanz',
            name='num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
