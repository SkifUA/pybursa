# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50, null=True, blank=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('package', models.CharField(max_length=10, choices=[(b'Gold', b'Gold'), (b'Standart', b'Standart'), (b'VIP', b'VIP')])),
                ('courses', models.ManyToManyField(to='courses.Course')),
                ('dossier', models.ForeignKey(to='dossier.Dossier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
