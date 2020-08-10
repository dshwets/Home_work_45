from django import forms
from .models import Statuses, Issues, TO_DO_List


class DateInput(forms.DateInput):
    input_type = 'date'


class ToDoForm(forms.ModelForm):

    class Meta:
        model = TO_DO_List
        fields = ['summary', 'description', 'status', 'issue']
        widgets ={'issue': forms.CheckboxSelectMultiple}