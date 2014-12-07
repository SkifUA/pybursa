# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='job_title',
            field=models.CharField(max_length=10, choices=[(b't', b'teacher'), (b'a', b'assistant')]),
            preserve_default=True,
        ),
    ]
