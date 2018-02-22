# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0003_dev_time_dev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='online_time',
            field=models.CharField(default=b'-', max_length=512, blank=True),
        ),
    ]
