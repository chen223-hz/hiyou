# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0046_remove_fenlei_scenic_fenlei'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wxscenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.ForeignKey(to='scenic.Point', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Wxusername',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'-', max_length=100, blank=True)),
                ('wxid', models.CharField(default=b'-', max_length=150, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='wxscenic',
            name='wxuser',
            field=models.ForeignKey(to='scenic.Wxusername', null=True),
        ),
    ]
