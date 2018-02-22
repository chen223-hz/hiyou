# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0017_auto_20170512_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'-', max_length=512, blank=True)),
                ('scenic_facilities', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.TextField(null=True, blank=True)),
                ('facilities_point', models.ForeignKey(to='scenic.Facilities', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
