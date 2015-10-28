# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina_principal',
            name='imagen_litigios',
        ),
        migrations.RemoveField(
            model_name='pagina_principal',
            name='imagen_propiedad_intelectual',
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='iimagen_litigios',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='pagina_principal',
            name='imagen_propiedad',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_articulos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_internacional',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_negocios',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_slide',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
        migrations.AlterField(
            model_name='pagina_principal',
            name='imagen_video',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
    ]
