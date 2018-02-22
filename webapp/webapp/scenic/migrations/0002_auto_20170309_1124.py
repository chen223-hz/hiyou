# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='ssid',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='scenic',
            name='ssid',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
