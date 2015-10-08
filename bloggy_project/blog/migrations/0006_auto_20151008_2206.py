# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_markdown.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151008_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=django_markdown.models.MarkdownField(default=datetime.datetime(2015, 10, 8, 20, 6, 53, 641311, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
