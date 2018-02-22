# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0025_domain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='area_domain',
            new_name='area_domai',
        ),
    ]
