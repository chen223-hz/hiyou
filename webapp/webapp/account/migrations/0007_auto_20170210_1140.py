# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_group_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='role',
            field=models.CharField(max_length=100, verbose_name='\u89d2\u8272'),
        ),
    ]
