# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acerca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='conducta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='membresias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='reconocimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('texto_descripcion', redactor.fields.RedactorField(default=b' ', verbose_name='Contenido')),
            ],
        ),
    ]
