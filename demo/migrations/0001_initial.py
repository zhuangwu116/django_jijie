# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u5b57')),
            ],
            options={
                'db_table': 'demo_author',
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.BooleanField(choices=[(0, '\u7537'), (1, '\u5973')], max_length=1, verbose_name='\u6027\u522b')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('address', models.CharField(max_length=50, verbose_name='\u4f4f\u5740')),
                ('birthday', models.DateField(verbose_name='\u51fa\u751f\u65e5\u671f')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='demo.Author', verbose_name='\u4f5c\u8005')),
            ],
            options={
                'db_table': 'demo_authordetail',
                'verbose_name': '\u4f5c\u8005\u8be6\u60c5',
                'verbose_name_plural': '\u4f5c\u8005\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u4e66\u540d')),
                ('publication_date', models.DateField(verbose_name='\u51fa\u7248\u65e5\u671f')),
                ('price', models.DecimalField(decimal_places=2, default=10, max_digits=5, verbose_name='\u4ef7\u683c')),
                ('authors', models.ManyToManyField(to='demo.Author', verbose_name='\u4f5c\u8005')),
            ],
            options={
                'db_table': 'demo_book',
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('address', models.CharField(max_length=50, verbose_name='\u5730\u5740')),
                ('city', models.CharField(max_length=60, verbose_name='\u5e02')),
                ('state_province', models.CharField(max_length=30, verbose_name='\u7701')),
                ('country', models.CharField(max_length=50, verbose_name='\u56fd\u5bb6')),
                ('website', models.URLField(verbose_name='\u7f51\u5740')),
            ],
            options={
                'db_table': 'demo_publisher',
                'verbose_name': '\u51fa\u7248\u793e',
                'verbose_name_plural': '\u51fa\u7248\u793e',
            },
            managers=[
                ('publisherLists', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Publisher', verbose_name='\u51fa\u7248\u793e'),
        ),
    ]
