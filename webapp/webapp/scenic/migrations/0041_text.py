# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0040_auto_20170711_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(default=b'-', max_length=512, blank=True)),
                ('direct', models.CharField(default=b'-', max_length=512, blank=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
