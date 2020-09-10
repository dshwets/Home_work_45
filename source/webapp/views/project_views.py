from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.models import TO_DO_List, Project
from webapp.forms import ToDoForm, SeacrhForm, ProjectForm, ManageTeamForm


class Project_view(ListView):
    template_name = 'project/projects.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class Watch_project_view(DetailView):
    template_name = 'project/watch_project.html'
    model = Project

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.is_active:
            raise Http404
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class Create_project_view(PermissionRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create_project.html'
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('watch_project', kwargs={'pk': self.object.pk})


class ProjectToDoCreateView(PermissionRequiredMixin, CreateView):
    model = TO_DO_List
    form_class = ToDoForm
    template_name = 'todo/create_todo_action.html'
    permission_required = 'webapp.add_to_do_list'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        to_do_action = form.save(commit=False)
        to_do_action.project = project
        to_do_action.save()
        form.save_m2m()
        return redirect('watch_project', pk=project.pk)

    def has_permission(self):
        return super().has_permission() and (self.request.user in get_object_or_404(Project, pk=self.kwargs.get('pk')).team.all())


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/update_project.html'
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('watch_project', kwargs={'pk': self.object.pk})


class ManageTeamView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ManageTeamForm
    template_name = 'project/manage_team.html'
    permission_required = 'webapp.can_change_team'

    def get_success_url(self):
        return reverse('watch_project', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and (self.request.user in self.get_object().team.all())


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('projects')
    permission_required = 'webapp.delete_project'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = super().get_success_url()
        print(self.object.is_active)
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)
