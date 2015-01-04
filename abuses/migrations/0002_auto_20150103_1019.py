# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_slug'),
        ('courses', '0002_course_slug'),
        ('coaches', '0001_initial'),
        ('abuses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abuse',
            name='email',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='name_student',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='name_teach',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='text',
        ),
        migrations.RemoveField(
            model_name='abuse',
            name='topic',
        ),
        migrations.AddField(
            model_name='abuse',
            name='courses',
            field=models.ForeignKey(default=1, to='courses.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abuse',
            name='name',
            field=models.ForeignKey(default=1, to='coaches.Coach'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abuse',
            name='surname',
            field=models.ForeignKey(default=2, to='students.Student'),
            preserve_default=False,
        ),
    ]
