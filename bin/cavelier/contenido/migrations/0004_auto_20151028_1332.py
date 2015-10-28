# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_auto_20151028_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_articulos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_slide',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_video',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
