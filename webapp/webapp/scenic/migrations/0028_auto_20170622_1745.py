# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0027_auto_20170622_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='area_domain',
            field=models.ForeignKey(to='scenic.Area', null=True),
        ),
    ]
