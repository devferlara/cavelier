# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_remove_generales_gaspar'),
    ]

    operations = [
        migrations.AddField(
            model_name='generales',
            name='copyright',
            field=models.CharField(default=b' ', max_length=80),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_cinco',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_cuatro',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_dos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_seis',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_tres',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='premio_logo_uno',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AddField(
            model_name='generales',
            name='texto_bogota',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Texto Bogota'),
        ),
        migrations.AddField(
            model_name='generales',
            name='texto_medellin',
            field=redactor.fields.RedactorField(default=b' ', verbose_name='Texto Medellin'),
        ),
        migrations.AddField(
            model_name='generales',
            name='union_logos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
    ]
