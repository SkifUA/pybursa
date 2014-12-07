# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(max_length=10, choices=[(b'Gold', b'Gold'), (b'Standart', b'Standart'), (b'VIP', b'VIP')]),
            preserve_default=True,
        ),
    ]
