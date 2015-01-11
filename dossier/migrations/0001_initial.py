# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=15, choices=[(b'red', b'red'), (b'orange', b'orange'), (b'yellow', b'yellow'), (b'green', b'green'), (b'blue', b'blue'), (b'pink', b'pink'), (b'violet', b'violet')])),
                ('address', models.ForeignKey(to='address.Addres')),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
