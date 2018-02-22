# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0029_point_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='ba',
        ),
        migrations.RemoveField(
            model_name='point',
            name='geshu',
        ),
    ]
