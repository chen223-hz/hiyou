# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0054_auto_20170821_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=512, null=True, blank=True)),
                ('statrtime', models.CharField(max_length=512, null=True, blank=True)),
                ('endtime', models.CharField(max_length=512, null=True, blank=True)),
                ('signal', models.CharField(max_length=512, null=True, blank=True)),
                ('num', models.IntegerField(null=True, blank=True)),
                ('typee', models.CharField(max_length=512, null=True, blank=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
                ('tanz', models.ForeignKey(to='scenic.Tanz', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
