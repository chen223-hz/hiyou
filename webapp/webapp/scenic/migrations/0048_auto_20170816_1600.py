# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0047_auto_20170801_0918'),
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
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tanz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='tanz',
            field=models.ForeignKey(to='scenic.Tanz', null=True),
        ),
    ]
