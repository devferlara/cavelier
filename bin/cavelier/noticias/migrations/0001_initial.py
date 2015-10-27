# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticias_web',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to=b'photos')),
                ('contenido', redactor.fields.RedactorField(default=b' ', verbose_name='Contenido')),
            ],
        ),
    ]
