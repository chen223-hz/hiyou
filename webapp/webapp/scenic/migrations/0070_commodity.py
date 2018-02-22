# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0069_userinfo_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
                ('stock', models.IntegerField(null=True, blank=True)),
                ('sales', models.IntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
        ),
    ]
