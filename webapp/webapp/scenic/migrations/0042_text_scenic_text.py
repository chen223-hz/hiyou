# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0041_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='scenic_text',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
