# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0020_point_ba'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='geshu',
            field=models.CharField(default=b'-', max_length=512, blank=True),
        ),
    ]
