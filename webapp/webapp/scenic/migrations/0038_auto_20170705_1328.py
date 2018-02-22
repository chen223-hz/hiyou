# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0037_area_zhu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
