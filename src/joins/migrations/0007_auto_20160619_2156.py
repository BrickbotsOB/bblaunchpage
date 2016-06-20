# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0006_join_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='first_name',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='join',
            name='last_name',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
    ]
