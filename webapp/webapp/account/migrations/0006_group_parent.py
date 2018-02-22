# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_group_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(related_name='children', to='account.Group', null=True),
        ),
    ]
