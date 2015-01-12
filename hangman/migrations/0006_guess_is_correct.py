# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0005_remove_game_guess_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='guess',
            name='is_correct',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
