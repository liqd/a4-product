# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 09:02
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'a4_candy_cms_pages'
         WHERE app_label = 'liqd_product_cms_pages';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'liqd_product_cms_pages';
                 WHERE app_label = 'a4_candy_cms_pages';"""


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_pages', '0004_add_fields_to_hompage'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
