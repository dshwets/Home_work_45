from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode

from webapp.models import TO_DO_List, Project
from webapp.forms import ToDoForm, SeacrhForm
from django.views.generic import View, TemplateView, FormView, ListView
from django.urls import reverse


class Project_view(ListView):
    template_name = 'project/projects.html'
    model = Project
    context_object_name = 'projects'
