# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lineas_de_servicio', '0003_linea_de_servicio_imagen_interna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea_individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', redactor.fields.RedactorField(default=b' ', verbose_name='Descripcion')),
            ],
        ),
    ]
