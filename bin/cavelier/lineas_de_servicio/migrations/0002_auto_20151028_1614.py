# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lineas_de_servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linea_de_servicio',
            name='texto_lema',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Lema'),
        ),
    ]
