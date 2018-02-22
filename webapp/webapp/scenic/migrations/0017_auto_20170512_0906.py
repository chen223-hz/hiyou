# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0016_dev_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='isonline',
            field=models.BooleanField(default=False),
        ),
    ]
