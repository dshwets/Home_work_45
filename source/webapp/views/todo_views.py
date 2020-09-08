from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.views.generic import View, TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.models import TO_DO_List, Project
from webapp.forms import ToDoForm, SeacrhForm


class SeacrhView(ListView):
    def get_search_form(self):
        return SeacrhForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
                return self.form.cleaned_data['search']
        return None

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = self.get_query()
            queryset = queryset.filter(query)

        queryset = queryset.filter(project__is_active=True)
        return queryset

    def get_query(self):
        self.query= Q()
        return self.query



class IndexView(SeacrhView):
    template_name = 'todo/index.html'
    model = TO_DO_List
    context_object_name = 'to_do_list'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get_query(self):
        self.query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
        return self.query


class DeleteTodoView(PermissionRequiredMixin, DeleteView):
    model = TO_DO_List
    context_object_name = 'todo_action'
    template_name = 'todo/delete.html'
    permission_required = 'webapp.delete_to_do_list'

    def get_success_url(self):
        return reverse('watch_project', kwargs={'pk': self.object.project.pk})

    def has_permission(self):
        return super().has_permission() and (self.request.user in self.get_object().project.team.all())


class CreateTodoView(PermissionRequiredMixin, CreateView):
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


class WatchTodoView(TemplateView):
    template_name = 'todo/view_to_do_action.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_action'] = get_object_or_404(TO_DO_List, pk=kwargs['pk'])
        if not context['to_do_action'].project.is_active:
            raise Http404
        return context


class UpdateTodoView(PermissionRequiredMixin, UpdateView):
    template_name = 'todo/update_to_do_action.html'
    form_class = ToDoForm
    model = TO_DO_List
    permission_required = 'webapp.change_to_do_list'

    def get_success_url(self):
        return reverse('watch_todo', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and (self.request.user in self.get_object().project.team.all())
