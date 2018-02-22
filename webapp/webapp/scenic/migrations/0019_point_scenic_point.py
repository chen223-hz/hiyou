# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0018_facilities_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='scenic_point',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
