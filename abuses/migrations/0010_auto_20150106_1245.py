# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0009_abuse'),
    ]

    operations = [
        migrations.AddField(
            model_name='abuse',
            name='email_teach',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email_DB'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='email',
            field=models.EmailField(max_length=254, null=True),
            preserve_default=True,
        ),
    ]
