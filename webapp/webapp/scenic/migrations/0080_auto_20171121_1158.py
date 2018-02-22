# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0079_auto_20171121_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity_group',
            name='commodity',
        ),
        migrations.AddField(
            model_name='commodity',
            name='group',
            field=models.ForeignKey(to='scenic.Commodity_Group', null=True),
        ),
    ]
