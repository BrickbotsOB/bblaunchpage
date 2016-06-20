# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20160610_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
        ),
    ]
