# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0015_auto_20151028_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abogado_individual',
            old_name='nombre',
            new_name='apellidos',
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='nombres',
            field=models.CharField(default=datetime.datetime(2015, 10, 28, 14, 11, 31, 189512, tzinfo=utc), max_length=100),
            preserve_default=False,
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
        migrations.AlterField(
            model_name='abogado_individual',
            name='imagen',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
