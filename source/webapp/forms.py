from django import forms
from .models import Statuses, Issues


class DateInput(forms.DateInput):
    input_type = 'date'


class ToDoForm(forms.Form):
    summary = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea)
    description = forms.CharField(max_length=3000, required=False, label='Описание подробное', initial=None,
                                  widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Statuses.objects.all(), required=True, label='Статус', empty_label=None)
    issue = forms.ModelMultipleChoiceField(queryset=Issues.objects.all(), required=True, label='Тип задачи',
                                           widget=forms.CheckboxSelectMultiple)
