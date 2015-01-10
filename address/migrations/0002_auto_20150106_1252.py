# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addres',
            name='post_index',
            field=models.IntegerField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
    ]
