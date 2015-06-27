# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapeim', '0003_auto_20150601_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='state',
            field=models.IntegerField(choices=[(1, 'Disponible'), (2, 'Ocupado'), (3, 'Mantenimiento')], default=1),
        ),
        migrations.DeleteModel(
            name='ElementState',
        ),
    ]
