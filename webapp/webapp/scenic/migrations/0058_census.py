# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0057_userinfo_mac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Census',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vivo', models.IntegerField(null=True, blank=True)),
                ('apple', models.IntegerField(null=True, blank=True)),
                ('oppo', models.IntegerField(null=True, blank=True)),
                ('huawei', models.IntegerField(null=True, blank=True)),
                ('samsung', models.IntegerField(null=True, blank=True)),
                ('date', models.CharField(max_length=512, null=True, blank=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
