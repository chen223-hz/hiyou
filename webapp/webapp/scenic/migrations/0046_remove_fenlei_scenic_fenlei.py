# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0045_fenlei_scenic_fenlei'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fenlei',
            name='scenic_fenlei',
        ),
    ]
