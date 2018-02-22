# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0070_commodity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
