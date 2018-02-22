# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_group_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cellphone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
