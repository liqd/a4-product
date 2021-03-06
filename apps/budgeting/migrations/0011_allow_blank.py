# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('meinberlin_budgeting', '0011_allow_blank')]

    dependencies = [
        ('a4_candy_budgeting', '0010_add_default_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='moderator_statement',
            field=models.OneToOneField(null=True, related_name='+', to='a4_candy_moderatorfeedback.ModeratorStatement', blank=True, on_delete=models.CASCADE),
        ),
    ]
