# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_playlist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(),
        ),
    ]
