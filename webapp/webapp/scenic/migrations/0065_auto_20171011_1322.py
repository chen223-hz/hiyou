# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0064_newo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newo',
            name='date',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
