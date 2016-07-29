# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160409_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.CharField(help_text='link to event website', max_length=500, blank=True),
        ),
    ]
