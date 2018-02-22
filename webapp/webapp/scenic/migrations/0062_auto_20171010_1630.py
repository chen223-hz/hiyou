# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0061_census_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='census',
            name='dev',
        ),
        migrations.RemoveField(
            model_name='census',
            name='scenic',
        ),
        migrations.DeleteModel(
            name='Census',
        ),
    ]
