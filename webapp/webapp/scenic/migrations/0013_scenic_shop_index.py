# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0012_auto_20170329_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='shop_index',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
