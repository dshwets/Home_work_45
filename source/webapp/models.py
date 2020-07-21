from django.db import models


class TO_DO_List(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, null=False, blank=False, default='new', verbose_name='Статус')
    deadline = models.DateField(default=None, blank=True, null=True, verbose_name='Дата выполнения')

    def __str__(self):

        return "{}. {}".format(self.pk, self.description)
