# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0038_auto_20170705_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilities',
            name='leixing',
            field=models.CharField(default=b'-', max_length=512, null=True, blank=True),
        ),
    ]
