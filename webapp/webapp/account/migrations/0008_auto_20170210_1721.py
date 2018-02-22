# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20170210_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='role',
            field=models.SmallIntegerField(default=0, verbose_name='\u89d2\u8272'),
        ),
    ]
