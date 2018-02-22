# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0058_census'),
    ]

    operations = [
        migrations.AddField(
            model_name='census',
            name='Dev',
            field=models.ForeignKey(to='scenic.Dev', null=True),
        ),
    ]
