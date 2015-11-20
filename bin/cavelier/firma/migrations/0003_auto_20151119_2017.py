# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0002_auto_20151118_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='acerca',
            name='texto_descripcion_en',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Ingles'),
        ),
        migrations.AddField(
            model_name='acerca',
            name='texto_descripcion_fr',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Frances'),
        ),
        migrations.AddField(
            model_name='conducta',
            name='texto_descripcion_en',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Ingles'),
        ),
        migrations.AddField(
            model_name='conducta',
            name='texto_descripcion_fr',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Frances'),
        ),
        migrations.AddField(
            model_name='membresias',
            name='texto_descripcion_en',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Ingles'),
        ),
        migrations.AddField(
            model_name='membresias',
            name='texto_descripcion_fr',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Frances'),
        ),
        migrations.AddField(
            model_name='reconocimientos',
            name='texto_descripcion_en',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Ingles'),
        ),
        migrations.AddField(
            model_name='reconocimientos',
            name='texto_descripcion_fr',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Contenido Frances'),
        ),
    ]
