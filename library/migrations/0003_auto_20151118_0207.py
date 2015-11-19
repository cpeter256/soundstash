# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151112_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sound',
            old_name='uri',
            new_name='url',
        ),
    ]
