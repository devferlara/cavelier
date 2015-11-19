# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acerca',
            name='imagen_interna',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='conducta',
            name='imagen_interna',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='membresias',
            name='imagen_interna',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='reconocimientos',
            name='imagen_interna',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
