# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0010_auto_20150106_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abuse',
            name='email_teach',
        ),
    ]
