# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_generales_gaspar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generales',
            name='gaspar',
        ),
    ]
