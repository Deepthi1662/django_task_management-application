# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('task_type', models.CharField(choices=[('ONE_TIME', 'ONE_TIME'), ('REPEAT', 'REPEACT')], max_length=15)),
                ('completed', models.BooleanField(default=False)),
                ('image', models.FileField(blank=True, upload_to='hotels/')),
                ('video', models.FileField(blank=True, upload_to='hotels/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
