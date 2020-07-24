from django.db import models
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TO_DO_List(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, null=False, blank=False, default='new', verbose_name='Статус')
    deadline = models.DateField(default=None, blank=True, null=True, verbose_name='Дата выполнения', choices=STATUS_CHOICES)
    long_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание',
                                        default=None)

    def __str__(self):

        return "{}. {}".format(self.pk, self.description)
