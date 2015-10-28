# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_auto_20151028_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generales',
            name='imagen_internacional',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='imagen_litigios',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='imagen_negocios',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='imagen_propiedad',
        ),
    ]
