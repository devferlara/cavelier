# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_auto_20151028_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_cinco',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_cuatro',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_dos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_seis',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_tres',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='premio_logo_uno',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
