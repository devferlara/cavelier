# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_idiomas'),
        ('abogados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado_individual',
            name='Publicaciones',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='experiencia',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='formacion',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='idiomas',
            field=models.ManyToManyField(to='general.idiomas', blank=True),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='imagen',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='lema',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='mail',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='telefono_directo',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='telefonos',
            field=models.CharField(default=b' ', max_length=100),
        ),
    ]
