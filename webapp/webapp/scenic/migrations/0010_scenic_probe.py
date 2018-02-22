# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0009_auto_20170324_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='probe',
            field=models.TextField(null=True, blank=True),
        ),
    ]
