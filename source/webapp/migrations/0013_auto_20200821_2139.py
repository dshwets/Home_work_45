# Generated by Django 2.2 on 2020-08-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20200821_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Дата  окончания'),
        ),
    ]
