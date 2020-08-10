from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import TO_DO_List
from webapp.forms import ToDoForm
from django.views.generic import View, TemplateView, FormView
from django.urls import reverse



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_list'] = TO_DO_List.objects.all()
        return context


class DeleteTodoView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        return render(request, 'delete.html', context={'todo_action': todo_action})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        todo_action.delete()
        return redirect('index_view')


class CreateTodoView(FormView):
    template_name = 'create_todo_action.html'
    form_class = ToDoForm

    def form_valid(self, form):
        self.todo_action = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('watch_todo', kwargs={'pk': self.todo_action.pk})


class WatchTodoView(TemplateView):
    template_name = 'view_to_do_action.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_action'] = get_object_or_404(TO_DO_List, pk=kwargs['pk'])
        return context


class UpdateTodoView(FormView):
    template_name = 'update_to_do_action.html'
    form_class = ToDoForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print(kwargs)
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