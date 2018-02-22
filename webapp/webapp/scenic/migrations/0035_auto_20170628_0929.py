# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import webapp.scenic.models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0034_remove_facilities_scenic_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilities',
            name='list_icon',
            field=models.ImageField(null=True, upload_to=webapp.scenic.models.image_filename, blank=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='map_icon',
            field=models.ImageField(null=True, upload_to=webapp.scenic.models.image_filename, blank=True),
        ),
    ]
