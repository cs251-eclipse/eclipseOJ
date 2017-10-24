# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import judge.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to=judge.models.upload_to)),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('cpp', 'C++'), ('java', 'Java'), ('c', 'C'), ('py', 'Python 2'), ('py3', 'Python 3')], default='cpp', max_length=4)),
                ('testcases_passed', models.IntegerField(default=0)),
                ('verdict', models.CharField(choices=[('Q', 'In queue'), ('R', 'Running'), ('WA', 'Wrong Answer'), ('CE', 'Compilation Error'), ('RE', 'Runtime Error'), ('AC', 'Accepted'), ('TLE', 'Time Limit Exceeded')], default='Q', max_length=2)),
            ],
        ),
    ]
