# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0003_auto_20150103_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='abuse',
            name='text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(verbose_name=b'Name teach', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(verbose_name=b'Name student', to='students.Student'),
            preserve_default=True,
        ),
    ]
