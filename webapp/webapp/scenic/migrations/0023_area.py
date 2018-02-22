# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0022_auto_20170622_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'-', max_length=512, blank=True)),
                ('latitude', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('scenic_area', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
