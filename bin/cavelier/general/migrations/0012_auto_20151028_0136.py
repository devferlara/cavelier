# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20151028_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_uno',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'photos'),
        ),
    ]
