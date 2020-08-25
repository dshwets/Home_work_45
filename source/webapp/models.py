from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator, BaseValidator
from django.db import models
from django.utils.deconstruct import deconstructible

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


# @deconstructible
# class MinLengthValidator(BaseValidator):
#     message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
#     code = 'too_short'
#
#     def compare(self, value, limit):
#         return value < limit
#
#     def clean(self, value):
#         return len(value)
#
#
def at_least_10(string):
    if len(string) < 10:
        raise ValidationError('This value is too short!')


##TODO протестировать все валидаторы, понять плюсы и минусы каждого.


class TO_DO_List(models.Model):
    summary = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание:',
                               validators=[MinLengthValidator(10), ])
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание подробное:',
                                   default=None, validators=[at_least_10, ])
    status = models.ForeignKey('webapp.Statuses', related_name='statuses', on_delete=models.PROTECT,
                               verbose_name='Статус:')
    issue = models.ManyToManyField('webapp.Issues', related_name='issueses', blank=False, verbose_name='Тип задачи:')
    project = models.ForeignKey('webapp.Project', related_name='projects', on_delete=models.PROTECT,
                                verbose_name='Название проекта:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

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


class Project(models.Model):
    begin_date = models.DateField(verbose_name="Дата начала", null=False, blank=False)
    end_date = models.DateField(verbose_name="Дата  окончания", null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название проекта',
                             validators=[MinLengthValidator(10), ])
    description = models.TextField(max_length=3000, null=False, blank=False,verbose_name='Описание проекта',
                                   validators=[MinLengthValidator(10), ])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title