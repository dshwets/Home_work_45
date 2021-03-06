# Generated by Django 2.2 on 2020-08-21 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200815_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateTimeField(verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Дата начала')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Название проекта')),
                ('description', models.TextField(max_length=3000, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Описание проекта')),
            ],
        ),
    ]
