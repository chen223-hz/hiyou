# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0039_facilities_leixing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fenlei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'-', max_length=512, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='facilities',
            name='leixing',
            field=models.ForeignKey(to='scenic.Fenlei', null=True),
        ),
    ]
