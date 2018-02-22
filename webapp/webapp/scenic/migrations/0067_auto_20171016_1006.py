# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0066_auto_20171011_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='newo',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='endtime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='statrtime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
