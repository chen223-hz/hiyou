# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0082_auto_20171122_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='commodity_group',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
