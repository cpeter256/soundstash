# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('uri', models.URLField(unique=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(unique=True, max_length=200, primary_key=True, serialize=False)),
                ('sounds', models.ManyToManyField(to='library.Sound')),
            ],
        ),
    ]
