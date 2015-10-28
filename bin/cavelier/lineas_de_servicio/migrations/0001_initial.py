# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linea_de_servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('imagen', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('texto_lema', models.CharField(max_length=80)),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Descripcion')),
            ],
        ),
    ]
