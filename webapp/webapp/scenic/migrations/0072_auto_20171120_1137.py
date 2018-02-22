# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0071_auto_20171113_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity_Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='group',
            field=models.ForeignKey(to='scenic.Commodity_Group', null=True),
        ),
    ]
