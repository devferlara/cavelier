# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0017_auto_20151028_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abogado_individual',
            old_name='nombres',
            new_name='nombre',
        ),
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
