# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-24 18:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_time', models.DateTimeField(verbose_name='回答時刻')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='選択肢本文')),
                ('correct', models.BooleanField(default=False, verbose_name='正解')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名前')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='問題文')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='クイズ名')),
                ('date', models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='実施日')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='クイズ開始時間')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Player')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Quiz'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.Result'),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('quiz', 'player')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('result', 'choice')]),
        ),
    ]