from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode

from webapp.models import TO_DO_List, Project
from webapp.forms import ToDoForm, SeacrhForm, ProjectForm
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView
from django.urls import reverse


class Project_view(ListView):
    template_name = 'project/projects.html'
    model = Project
    context_object_name = 'projects'


class Watch_project_view(DetailView):
    template_name = 'project/watch_project.html'
    model = Project



class Create_project_view(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create_project.html'

    def get_success_url(self):
        return reverse('watch_project', kwargs={'pk': self.object.pk})


class ProjectToDoCreateView(CreateView):
    model = TO_DO_List
    template_name = 'todo/create_todo_action.html'
    form_class = ToDoForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        to_do_action = form.save(commit=False)
        to_do_action.project = project
        to_do_action.save()
        form.save_m2m()
        return redirect('watch_project', pk=project.pk)