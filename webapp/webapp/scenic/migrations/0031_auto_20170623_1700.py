# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0030_auto_20170623_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
