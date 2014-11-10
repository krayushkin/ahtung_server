# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahtung_api', '0003_auto_20141107_0919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EnabledSignals',
            new_name='EnabledSignal',
        ),
    ]
