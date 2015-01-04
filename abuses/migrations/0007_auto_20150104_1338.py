# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0006_auto_20150103_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abuse',
            name='courses',
            field=models.ForeignKey(verbose_name='Course', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(verbose_name='To whom', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(verbose_name='Of whom', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='text',
            field=models.CharField(max_length=255, null=True, verbose_name='What made', blank=True),
            preserve_default=True,
        ),
    ]
