# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0078_auto_20171121_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='group',
        ),
        migrations.AddField(
            model_name='commodity_group',
            name='commodity',
            field=models.ForeignKey(to='scenic.Commodity', null=True),
        ),
    ]
