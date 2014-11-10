# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahtung_api', '0004_auto_20141107_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='signal_id',
            field=models.CharField(default=1, unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
