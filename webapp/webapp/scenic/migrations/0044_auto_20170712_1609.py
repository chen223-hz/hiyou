# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import webapp.scenic.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0043_auto_20170712_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcontent',
            name='image',
            field=models.ImageField(null=True, upload_to=webapp.scenic.models.image_filename, blank=True),
        ),
        migrations.AddField(
            model_name='textcontent',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
