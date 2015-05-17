# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ag53', '0002_auto_20150517_0932'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.RemoveField(
            model_name='password',
            name='user',
        ),
        migrations.DeleteModel(
            name='Password',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='user',
            new_name='profile',
        ),
    ]
