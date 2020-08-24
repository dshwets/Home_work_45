from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode

from webapp.models import TO_DO_List, Project
from webapp.forms import ToDoForm, SeacrhForm
from django.views.generic import View, TemplateView, FormView, ListView, CreateView
from django.urls import reverse


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
            pass
            query = self.get_query()
            queryset = queryset.filter(query)
        return queryset

    def get_query(self):
        self.query= Q()
        return self.query



class IndexView(SeacrhView):
    template_name = 'todo/index.html'
    model = TO_DO_List
    context_object_name = 'to_do_list'
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1

    def get_query(self):
        self.query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
        return self.query


class DeleteTodoView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        return render(request, 'todo/delete.html', context={'todo_action': todo_action})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        todo_action.delete()
        return redirect('index_view')


class CreateTodoView(CreateView):
    model = TO_DO_List
    form_class = ToDoForm
    template_name = 'todo/create_todo_action.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        to_do_action = form.save(commit=False)
        to_do_action.project = project
        to_do_action.save()
        form.save_m2m()
        return redirect('watch_project', pk=project.pk)

    # def get_success_url(self):
    #     return reverse('watch_todo', kwargs={'pk': self.object.pk})


class WatchTodoView(TemplateView):
    template_name = 'todo/view_to_do_action.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_action'] = get_object_or_404(TO_DO_List, pk=kwargs['pk'])
        return context


class UpdateTodoView(FormView):
    template_name = 'todo/update_to_do_action.html'
    form_class = ToDoForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('initial')
        kwargs['instance'] = self.todo_action
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_action'] = self.todo_action
        return context

    def form_valid(self, form):
        self.todo_action = form.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.todo_action = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TO_DO_List, pk=pk)

    def get_success_url(self):
        return reverse('watch_todo', kwargs={'pk': self.todo_action.pk})
