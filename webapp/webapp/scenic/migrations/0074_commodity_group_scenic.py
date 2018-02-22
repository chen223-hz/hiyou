# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0073_commodity_grounding'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity_group',
            name='scenic',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
