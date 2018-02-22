# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0032_auto_20170626_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
