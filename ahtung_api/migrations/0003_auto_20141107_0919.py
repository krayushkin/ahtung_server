# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahtung_api', '0002_auto_20141106_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnabledSignals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enabledsignals',
            name='group',
            field=models.ForeignKey(to='ahtung_api.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enabledsignals',
            name='signal',
            field=models.ForeignKey(to='ahtung_api.Signal'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='person',
            name='group_id',
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(default=1, to='ahtung_api.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='registration_id',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
