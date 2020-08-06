from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TO_DO_List(models.Model):
    summary = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание подробное',
                                        default=None)
    status = models.ForeignKey('webapp.Statuses', related_name='statuses', on_delete=models.PROTECT,
                               verbose_name='Статус')
    issue = models.ManyToManyField('webapp.Issues', related_name='issueses', blank=False, verbose_name='Тип задачи')


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)


class Statuses(models.Model):
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус')

    def __str__(self):
        return self.status


class Issues(models.Model):
    issue = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус')

    def __str__(self):
        return self.issue
