# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('cellphone', models.CharField(unique=True, max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('wechatUNID', models.CharField(max_length=64, verbose_name='\u5fae\u4fe1ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='\u6635\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.SmallIntegerField(default=0, verbose_name='\u89d2\u8272')),
                ('name', models.CharField(max_length=100, verbose_name='\u7ec4\u540d\u79f0')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(to='account.Group'),
        ),
    ]
