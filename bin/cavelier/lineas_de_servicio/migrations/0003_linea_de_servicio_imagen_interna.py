# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineas_de_servicio', '0002_auto_20151028_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='linea_de_servicio',
            name='imagen_interna',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
