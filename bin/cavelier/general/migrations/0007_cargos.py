# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_idiomas'),
    ]

    operations = [
        migrations.CreateModel(
            name='cargos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(default=b' ', max_length=80)),
            ],
        ),
    ]
