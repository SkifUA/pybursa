# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0002_auto_20150103_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(db_column=b'Name teach', to='coaches.Coach', help_text=b'Name teach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(help_text=b'Name student', to='students.Student'),
            preserve_default=True,
        ),
    ]
