# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20151028_1331'),
        ('abogados', '0019_auto_20151028_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado_individual',
            name='areas_practica',
            field=models.ManyToManyField(to='general.Areas_de_practica', blank=True),
        ),
        migrations.RemoveField(
            model_name='abogado_individual',
            name='cargo',
        ),
        migrations.AddField(
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
