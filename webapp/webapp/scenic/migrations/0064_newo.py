# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0063_census'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xin', models.IntegerField(null=True, blank=True)),
                ('lao', models.IntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('scenic', models.ForeignKey(to='scenic.Scenic', null=True)),
            ],
        ),
    ]
