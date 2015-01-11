# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tehnology', models.CharField(max_length=10, choices=[(b'python', b'python'), (b'JS', b'JS'), (b'rubybursa', b'rubybursa')])),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('teacher', models.CharField(max_length=150, null=True, blank=True)),
                ('assistent', models.CharField(max_length=150, null=True, blank=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
