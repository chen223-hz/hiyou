# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0067_auto_20171016_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='endtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='statrtime',
            field=models.DateTimeField(null=True),
        ),
    ]
