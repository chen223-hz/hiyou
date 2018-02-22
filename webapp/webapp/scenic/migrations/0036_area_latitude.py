# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0035_auto_20170628_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='latitude',
            field=models.TextField(null=True, blank=True),
        ),
    ]
