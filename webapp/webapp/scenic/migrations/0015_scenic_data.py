# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0014_scenic_template_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='data',
            field=models.TextField(null=True, blank=True),
        ),
    ]
