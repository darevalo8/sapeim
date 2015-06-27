# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('bland_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('document_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('serial_sena', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('features', models.TextField(blank=True)),
                ('bland', models.ForeignKey(to='sapeim.Bland')),
            ],
        ),
        migrations.CreateModel(
            name='ElementState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('state', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('element_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('hora_inicio', models.TimeField(blank=True)),
                ('hora_fin', models.TimeField(blank=True)),
                ('devolucion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('apellido', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('documento', models.IntegerField(null=True, blank=True)),
                ('document_type', models.ForeignKey(to='sapeim.DocumentType')),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='user',
            field=models.ForeignKey(to='sapeim.UserProfile'),
        ),
        migrations.AddField(
            model_name='element',
            name='element_type',
            field=models.ForeignKey(to='sapeim.ElementType'),
        ),
        migrations.AddField(
            model_name='element',
            name='state',
            field=models.ForeignKey(to='sapeim.ElementState'),
        ),
        migrations.AddField(
            model_name='detalleprestamo',
            name='element',
            field=models.ForeignKey(to='sapeim.Element'),
        ),
        migrations.AddField(
            model_name='detalleprestamo',
            name='prestamo',
            field=models.ForeignKey(to='sapeim.Prestamo'),
        ),
    ]
