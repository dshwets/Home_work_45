# Generated by Django 2.2 on 2020-07-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200721_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='deadline',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
    ]
