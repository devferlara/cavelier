# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20151028_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='generales',
            name='imagen_internacional',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='generales',
            name='imagen_litigios',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='generales',
            name='imagen_negocios',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
        migrations.AddField(
            model_name='generales',
            name='imagen_propiedad',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'uploads'),
        ),
    ]
