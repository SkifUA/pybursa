# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_slug'),
        ('courses', '0002_course_slug'),
        ('coaches', '0001_initial'),
        ('abuses', '0008_auto_20150104_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abuse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('text', models.CharField(max_length=255, null=True, verbose_name='What made', blank=True)),
                ('courses', models.ForeignKey(verbose_name='Course', to='courses.Course')),
                ('name', models.ForeignKey(verbose_name='To whom', to='coaches.Coach')),
                ('surname', models.ForeignKey(verbose_name='Of whom', to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
