# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0068_auto_20171016_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
