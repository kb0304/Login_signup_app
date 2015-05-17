# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('enrollment_no', models.IntegerField()),
                ('about_me', models.CharField(max_length=5000)),
                ('profile_pic', models.ImageField(upload_to=b'/ag53/images/profile_pic/')),
                ('cover_pic', models.ImageField(upload_to=b'/ag53/images/cover_pic/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='password',
            name='user',
            field=models.ForeignKey(to='ag53.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gender',
            name='user',
            field=models.ManyToManyField(to='ag53.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='user',
            field=models.ForeignKey(to='ag53.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branch',
            name='user',
            field=models.ManyToManyField(to='ag53.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='age',
            name='user',
            field=models.ManyToManyField(to='ag53.User'),
            preserve_default=True,
        ),
    ]
