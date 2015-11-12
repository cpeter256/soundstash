# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151112_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(serialize=False, primary_key=True, unique=True, max_length=200)),
                ('sounds', models.ManyToManyField(to='library.Sound')),
            ],
        ),
    ]
