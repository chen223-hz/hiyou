# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0028_auto_20170622_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='name',
            field=models.CharField(default=b'-', max_length=512, blank=True),
        ),
    ]
