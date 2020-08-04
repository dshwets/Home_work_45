from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class DateInput(forms.DateInput):
    input_type = 'date'


class ToDoForm(forms.Form):
    summary = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea)
    long_description = forms.CharField(max_length=3000, required=False, label='Описание подробное', initial=None,
                                       widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    deadline = forms.DateField(required=False, initial=None, label='Дата выполнения', widget=DateInput)
