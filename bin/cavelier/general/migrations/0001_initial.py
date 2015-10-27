# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('logo_general', models.ImageField(upload_to=b'photos')),
                ('link_facebook', models.CharField(max_length=100, validators=[django.core.validators.URLValidator()])),
                ('link_twitter', models.CharField(max_length=100, validators=[django.core.validators.URLValidator()])),
                ('link_linkedn', models.CharField(max_length=100, validators=[django.core.validators.URLValidator()])),
                ('link_instagram', models.CharField(max_length=100, validators=[django.core.validators.URLValidator()])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
