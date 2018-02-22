# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0024_auto_20170622_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.TextField(null=True)),
                ('area_domain', models.ForeignKey(to='scenic.Facilities', null=True)),
                ('scenic_domain', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
