# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0008_auto_20151028_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado_individual',
            name='areas_practica',
            field=models.ManyToManyField(to='general.Areas_de_practica', blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='cargo',
            field=models.OneToOneField(null=True, blank=True, to='general.Cargos'),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='idiomas',
            field=models.ManyToManyField(to='general.Idiomas', blank=True),
        ),
    ]
