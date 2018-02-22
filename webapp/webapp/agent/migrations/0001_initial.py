# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_headimgurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, verbose_name='\u4ee3\u7406\u5546\u540d\u79f0', blank=True)),
                ('username', models.CharField(max_length=512, null=True, verbose_name='\u624b\u673a\u8d26\u53f7', blank=True)),
                ('isdel', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('latitude', models.CharField(default=b'-', max_length=512, null=True, blank=True)),
                ('gaent', models.ForeignKey(to='account.Group', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
