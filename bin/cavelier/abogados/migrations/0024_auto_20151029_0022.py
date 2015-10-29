# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0017_areas_de_practica_en_areas_de_practica_fr_cargos_en_cargos_fr'),
        ('abogados', '0023_auto_20151029_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado_individual',
            name='Publicaciones_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones Frances'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='Publicaciones_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Publicaciones Ingles'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='areas_practica_frances',
            field=models.ManyToManyField(to='general.Areas_de_practica_fr', blank=True),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='areas_practica_ingles',
            field=models.ManyToManyField(to='general.Areas_de_practica_en', blank=True),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='cargo_en',
            field=models.ManyToManyField(to='general.Cargos_en', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='cargo_fr',
            field=models.ManyToManyField(to='general.Cargos_fr', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='experiencia_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Frances'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='experiencia_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Experiencia Laboral Ingles'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='formacion_frances',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica Frances'),
        ),
        migrations.AddField(
            model_name='abogado_individual',
            name='formacion_ingles',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Formacion academica Ingles'),
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
            name='idiomas',
            field=models.ManyToManyField(to='general.Idiomas', blank=True),
        ),
    ]
