# Generated by Django 2.2 on 2020-07-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200721_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='deadline',
            field=models.DateField(default=None, verbose_name='Дата выполнения'),
        ),
    ]
