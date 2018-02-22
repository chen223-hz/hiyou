# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0013_scenic_shop_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='template_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
