from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(models.Model):
    user: AbstractUser = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватара')
    about = models.TextField(max_length=2000, null=True, blank=True, verbose_name='О себе', default=None)
    github_account = models.URLField(max_length=150, null=True, blank=True, verbose_name='Гитхаб ауукант')


    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name ='Профиль'
        verbose_name_plural = 'Профили'