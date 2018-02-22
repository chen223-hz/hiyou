# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0077_auto_20171121_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='image',
            field=models.TextField(null=True, blank=True),
        ),
    ]
