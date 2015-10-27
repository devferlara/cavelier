# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_areas_de_practica'),
    ]

    operations = [
        migrations.CreateModel(
            name='abogado_individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('areas_practica', models.ManyToManyField(to='general.areas_de_practica', blank=True)),
            ],
        ),
    ]
