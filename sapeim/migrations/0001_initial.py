# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bland',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('bland_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('state', models.IntegerField(choices=[(1, 'Disponible'), (2, 'Ocupado'), (3, 'Mantenimiento')], default=1)),
                ('serial_sena', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('features', models.TextField(blank=True)),
                ('bland', models.ForeignKey(to='sapeim.Bland')),
            ],
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('element_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('devolucion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('apellido', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('document_type', models.IntegerField(choices=[(1, 'CC'), (2, 'Pasaporte'), (3, 'TI')], default=1)),
                ('documento', models.IntegerField(unique=True)),
                ('role', models.ForeignKey(to='sapeim.Role')),
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
