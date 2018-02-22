# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0005_auto_20170320_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=512, null=True, blank=True)),
                ('tid', models.CharField(max_length=512, null=True, blank=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
