# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Treasures',
            new_name='Treasure',
        ),
        migrations.AlterModelTable(
            name='treasure',
            table='treasure',
        ),
    ]
