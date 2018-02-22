# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0004_auto_20170309_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='online_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
