# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20170213_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='headimgurl',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
