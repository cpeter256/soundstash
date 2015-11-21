# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20151121_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
