# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 15:15
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'a4_candy_budgeting'
         WHERE app_label = 'liqd_product_budgeting';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'liqd_product_budgeting';
                 WHERE app_label = 'a4_candy_budgeting';"""


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_budgeting', '0021_update_content_types'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
