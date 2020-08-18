# Generated by Django 2.2 on 2020-08-14 18:24

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20200811_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=3000, null=True, validators=[webapp.models.at_least_10], verbose_name='Описание подробное'),
        ),
    ]