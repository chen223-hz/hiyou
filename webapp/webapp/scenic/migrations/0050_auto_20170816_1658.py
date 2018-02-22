# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0049_tanz_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tanz',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='tanz',
            name='scenic',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
