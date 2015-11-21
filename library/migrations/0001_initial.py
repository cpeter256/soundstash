# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=200)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='sound',
            field=models.ManyToManyField(to='library.Sound'),
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together=set([('name', 'owner')]),
        ),
    ]
