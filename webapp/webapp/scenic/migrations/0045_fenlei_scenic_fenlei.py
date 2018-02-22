# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0044_auto_20170712_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenlei',
            name='scenic_fenlei',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
