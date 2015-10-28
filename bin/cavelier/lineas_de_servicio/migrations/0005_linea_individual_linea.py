# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineas_de_servicio', '0004_linea_individual'),
    ]

    operations = [
        migrations.AddField(
            model_name='linea_individual',
            name='linea',
            field=models.ForeignKey(default=b'', blank=True, to='lineas_de_servicio.Linea_de_servicio'),
        ),
    ]
