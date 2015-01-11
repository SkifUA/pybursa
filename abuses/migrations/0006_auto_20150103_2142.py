# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0005_auto_20150103_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abuse',
            name='courses',
            field=models.ForeignKey(verbose_name='\u0421 \u043a\u0430\u043a\u043e\u0433\u043e \u043a\u0443\u0440\u0441\u0430', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='email',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(verbose_name='\u041a\u043e\u043c\u0443 \u0441\u0442\u0443\u0447\u0438\u043c', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(verbose_name='\u041d\u0430 \u043a\u043e\u0433\u043e \u0441\u0442\u0443\u0447\u0438\u043c', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='text',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0427\u0442\u043e \u043d\u0430\u0442\u0432\u043e\u0440\u0438\u043b', blank=True),
            preserve_default=True,
        ),
    ]
