# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-25 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0003_auto_20190125_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'ordering': ['name'], 'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
    ]
