# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('name_cours', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=1, choices=[(b't', b'teacher'), (b'a', b'assistant')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
