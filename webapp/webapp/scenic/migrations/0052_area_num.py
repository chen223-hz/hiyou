# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0051_tanz_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
