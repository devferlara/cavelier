# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generales',
            name='gaspar',
            field=models.CharField(default=b'gasparcito', max_length=80),
        ),
    ]
