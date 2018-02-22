# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0081_auto_20171121_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='grounding',
            field=models.CharField(default=False, max_length=512, blank=True),
        ),
    ]
