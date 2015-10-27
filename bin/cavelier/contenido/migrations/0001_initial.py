# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pagina_principal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen_slide', models.ImageField(upload_to=b'photos')),
                ('imagen_litigios', models.ImageField(upload_to=b'photos')),
                ('imagen_negocios', models.ImageField(upload_to=b'photos')),
                ('imagen_propiedad_intelectual', models.ImageField(upload_to=b'photos')),
                ('imagen_internacional', models.ImageField(upload_to=b'photos')),
                ('imagen_video', models.ImageField(upload_to=b'photos')),
                ('imagen_articulos', models.ImageField(upload_to=b'photos')),
            ],
        ),
    ]
