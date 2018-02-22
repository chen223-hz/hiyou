# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0006_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='openId',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
