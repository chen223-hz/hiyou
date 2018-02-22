# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0042_text_scenic_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(default=b'-', max_length=512, blank=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['num'],
            },
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['num']},
        ),
        migrations.AddField(
            model_name='textcontent',
            name='scenic_text',
            field=models.ForeignKey(to='scenic.Text', null=True),
        ),
    ]
