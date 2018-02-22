# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0050_auto_20170816_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanz',
            name='create',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
