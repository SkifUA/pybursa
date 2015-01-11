# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abuses', '0004_auto_20150103_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='abuse',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='Imail \u0443\u0447\u0438\u0442\u0435\u043b\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='courses',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(verbose_name='\u0418\u043c\u044f \u0443\u0447\u0438\u0442\u0435\u043b\u044f', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(verbose_name='\u0418\u043c\u044f \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abuse',
            name='text',
            field=models.TextField(null=True, verbose_name='\u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
