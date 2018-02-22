# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0055_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=512, null=True, blank=True)),
                ('nickname', models.CharField(max_length=512, null=True, blank=True)),
                ('sex', models.IntegerField(null=True, verbose_name='\u6027\u522b', blank=True)),
                ('city', models.CharField(max_length=512, null=True, blank=True)),
                ('country', models.CharField(max_length=512, null=True, blank=True)),
                ('province', models.CharField(max_length=512, null=True, blank=True)),
                ('headimgurl', models.CharField(max_length=512, null=True, blank=True)),
                ('subscribe_time', models.CharField(max_length=512, null=True, blank=True)),
                ('fbl', models.CharField(max_length=512, null=True, blank=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
