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
                ('imagen_interna', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('texto_lema', redactor.fields.RedactorField(default=b' ', verbose_name='Lema')),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Descripcion')),
                ('texto_descripcion_en', redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Ingles', blank=True)),
                ('texto_descripcion_fr', redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Ingles', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linea_general',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen_internacional', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_propiedad', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_negocios', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_litigios', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_internacional_en', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_propiedad_en', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_negocios_en', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_litigios_en', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_internacional_fr', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_propiedad_fr', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_negocios_fr', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
                ('imagen_litigios_fr', models.ImageField(default=b'imagen/default.png', upload_to=b'uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Linea_individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', redactor.fields.RedactorField(default=b' ', verbose_name='Descripcion')),
                ('linea', models.ForeignKey(default=b'', blank=True, to='lineas_de_servicio.Linea_de_servicio')),
            ],
        ),
    ]
