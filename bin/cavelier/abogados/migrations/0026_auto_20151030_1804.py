# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0025_auto_20151029_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado_individual',
            name='Publicaciones',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='Publicaciones_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones Frances', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='Publicaciones_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones Ingles', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='areas_practica',
            field=models.ManyToManyField(to='general.Areas_de_practica', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='cargo',
            field=models.ManyToManyField(to='general.Cargos', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='experiencia',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='experiencia_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Frances', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='experiencia_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Ingles', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='formacion',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='formacion_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica Frances', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='formacion_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica Ingles', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='idiomas',
            field=models.ManyToManyField(to='general.Idiomas', blank=True),
        ),
    ]
