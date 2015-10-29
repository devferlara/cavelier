# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0024_auto_20151029_0022'),
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
            field=models.ManyToManyField(to='general.Cargos', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='abogado_individual',
            name='idiomas',
            field=models.ManyToManyField(to='general.Idiomas', blank=True),
        ),
    ]
