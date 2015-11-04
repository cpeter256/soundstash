# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usr_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='first_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usr_first', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='last_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usr_last', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='password',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usr_pwd', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usr', models.CharField(max_length=200)),
            ],
        ),
    ]
