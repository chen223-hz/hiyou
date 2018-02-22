# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0019_point_scenic_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='ba',
            field=models.CharField(default=b'-', max_length=512, blank=True),
        ),
    ]
