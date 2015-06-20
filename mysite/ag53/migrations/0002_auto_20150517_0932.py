# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ag53.models


class Migration(migrations.Migration):

    dependencies = [
        ('ag53', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='age',
            name='user',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='user',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.ForeignKey(default=1, to='ag53.Age'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(default=1, to='ag53.Branch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(default=1, to='ag53.Gender'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='age',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch',
            field=models.CharField(default=b'default_value', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(default=b'd', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(default=b'default_value', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.CharField(default=b'default_value', max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_pic',
            field=models.ImageField(upload_to=ag53.models.rename_and_upload_cover_pic),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='enrollment_no',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'default_value', max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to=ag53.models.rename_and_upload_profile_pic),
            preserve_default=True,
        ),
    ]
