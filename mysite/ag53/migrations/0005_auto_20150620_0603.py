# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ag53', '0004_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
