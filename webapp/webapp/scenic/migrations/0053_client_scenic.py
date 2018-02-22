# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0052_area_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='scenic',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
