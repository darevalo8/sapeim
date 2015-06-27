# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapeim', '0002_auto_20150601_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(to='sapeim.Role', blank=True, null=True),
        ),
    ]
