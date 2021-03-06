# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 15:13
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'liqd_product_maps'
         WHERE app_label = 'meinberlin_maps';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'meinberlin_maps';
                 WHERE app_label = 'liqd_product_maps';"""


class Migration(migrations.Migration):

    replaces = [('liqd_product_maps', '0004_update_content_types')]

    dependencies = [
        ('a4_candy_maps', '0003_auto_20170420_1321'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
