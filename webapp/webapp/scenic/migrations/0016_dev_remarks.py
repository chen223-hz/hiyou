# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0015_scenic_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='remarks',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
