# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0007_auto_20150104_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abuse',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='name',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='surname',
        ),
        migrations.DeleteModel(
            name='Abuse',
        ),
    ]
