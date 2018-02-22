# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0080_auto_20171121_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='group',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
