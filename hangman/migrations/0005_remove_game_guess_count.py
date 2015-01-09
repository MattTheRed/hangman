# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0004_guess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='guess_count',
        ),
    ]
