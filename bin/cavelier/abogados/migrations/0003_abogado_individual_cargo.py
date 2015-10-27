# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_cargos'),
        ('abogados', '0002_auto_20151027_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado_individual',
            name='cargo',
            field=models.OneToOneField(null=True, blank=True, to='general.cargos'),
        ),
    ]
