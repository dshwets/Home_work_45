# Generated by Django 2.2 on 2020-09-12 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200911_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': {('can_watch_users', 'может видеть список пользователей')}, 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
