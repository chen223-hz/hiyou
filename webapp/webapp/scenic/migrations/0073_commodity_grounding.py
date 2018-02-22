# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0072_auto_20171120_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='grounding',
            field=models.BooleanField(default=False),
        ),
    ]
