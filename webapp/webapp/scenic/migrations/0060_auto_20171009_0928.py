# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0059_census_dev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='census',
            old_name='Dev',
            new_name='dev',
        ),
        migrations.AlterField(
            model_name='census',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
