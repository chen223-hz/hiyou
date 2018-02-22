# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import webapp.scenic.models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0031_auto_20170623_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='image',
            field=models.ImageField(null=True, upload_to=webapp.scenic.models.image_filename, blank=True),
        ),
        migrations.AddField(
            model_name='point',
            name='video',
            field=models.FileField(null=True, upload_to=webapp.scenic.models.video_filename, blank=True),
        ),
    ]
