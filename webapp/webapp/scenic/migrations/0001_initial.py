# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
        ('account', '0012_user_headimgurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(default=b'-', max_length=50, blank=True)),
                ('macaddr', models.CharField(max_length=20)),
                ('isonline', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('online_time', models.DateTimeField(null=True)),
                ('dev_type', models.CharField(max_length=400)),
                ('latitude', models.CharField(default=b'-', max_length=512, null=True, blank=True)),
                ('isdel', models.BooleanField(default=False)),
                ('agent_dev', models.ForeignKey(to='agent.Agent', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'-', max_length=512, blank=True)),
                ('latitude', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Scenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('num', models.IntegerField(null=True, verbose_name='\u6700\u5927\u4eba\u6570', blank=True)),
                ('isdel', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('latitude', models.TextField(null=True, blank=True)),
                ('authorizer_appid', models.CharField(max_length=512, null=True, blank=True)),
                ('authorizer_access_token', models.CharField(max_length=512, null=True, blank=True)),
                ('authorizer_refresh_token', models.CharField(max_length=512, null=True, blank=True)),
                ('nick_name', models.CharField(max_length=512, null=True, blank=True)),
                ('head_img', models.CharField(max_length=512, null=True, blank=True)),
                ('shop_id', models.CharField(max_length=512, null=True, blank=True)),
                ('mendian_name', models.CharField(max_length=512, null=True, blank=True)),
                ('qrcode_url', models.CharField(max_length=512, null=True, blank=True)),
                ('secretkey', models.CharField(max_length=512, null=True, blank=True)),
                ('agent', models.ForeignKey(to='agent.Agent', null=True)),
                ('group', models.ForeignKey(to='account.Group', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='region',
            name='scenic_region',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
        migrations.AddField(
            model_name='dev',
            name='region_dev',
            field=models.ForeignKey(to='scenic.Region', null=True),
        ),
        migrations.AddField(
            model_name='dev',
            name='scenic_dev',
            field=models.ForeignKey(to='scenic.Scenic', null=True),
        ),
    ]
