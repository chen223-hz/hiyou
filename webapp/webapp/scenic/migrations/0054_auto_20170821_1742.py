# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0053_client_scenic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='scenic',
        ),
        migrations.RemoveField(
            model_name='client',
            name='tanz',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
