# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_cargos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_cinco',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_cuatro',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_dos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_seis',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_tres',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='premio_logo_uno',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
        migrations.AlterField(
            model_name='generales',
            name='union_logos',
            field=models.ImageField(default=b'imagen/default.png', upload_to=b'static_in_pro/statis_in_root/uploads'),
        ),
    ]
