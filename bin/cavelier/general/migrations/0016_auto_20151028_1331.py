# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_auto_20151028_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_cinco',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_cuatro',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_dos',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_seis',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_tres',
        ),
        migrations.RemoveField(
            model_name='generales',
            name='premio_logo_uno',
        ),
    ]
