# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_group_cellphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='parent',
        ),
    ]
