# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tehnology',
            field=models.CharField(max_length=10, choices=[(b'python', b'python'), (b'JS', b'JS')]),
            preserve_default=True,
        ),
    ]
