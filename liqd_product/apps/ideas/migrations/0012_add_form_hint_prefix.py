# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 11:18
from __future__ import unicode_literals

import adhocracy4.images.fields
from django.db import migrations


class Migration(migrations.Migration):

    replaces = [('meinberlin_ideas', '0012_add_form_hint_prefix')]

    dependencies = [
        ('liqd_product_ideas', '0011_idea_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, help_prefix='Visualize your idea.', upload_to='ideas/images'),
        ),
    ]