# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_gameuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='user',
            field=models.ForeignKey(to='hangman.GameUser'),
            preserve_default=True,
        ),
    ]
