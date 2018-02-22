# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webapp.scenic.models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0076_auto_20171120_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='commodity',
            name='image',
            field=models.ImageField(null=True, upload_to=webapp.scenic.models.image_filename, blank=True),
        ),
    ]
