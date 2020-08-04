from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import TO_DO_List
from webapp.forms import ToDoForm
from django.views.generic import View,TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_list'] = TO_DO_List.objects.all()
        return context


class DeleteTodoView(View):
    def get(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        return render(request, 'delete.html', context={'todo_action': todo_action})
    def post(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        todo_action = get_object_or_404(TO_DO_List, pk=pk)
        todo_action.delete()
        return redirect('index_view')


class CreateTodoView(View):
    def get( self,request):
        if request.method == 'GET':
            return render(request, 'create_todo_action.html', context={
                'form': ToDoForm()
            })
    def post(self,request):
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            to_do_action = TO_DO_List.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                issue=form.cleaned_data['issue'],
                created_at=form.cleaned_data['created_at'],
            )
            return redirect('watch_todo', to_do_action.pk)
        else:
            return render(request,'create_todo_action.html', context={
                'form': form
            })


class WatchTodoView(TemplateView):
    template_name = 'view_to_do_action.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context['to_do_action'] = get_object_or_404(TO_DO_List, pk=kwargs['pk'])
        return context

# class UpdateTodoView(View):
def update_todo(request, pk):
    todo_action = get_object_or_404(TO_DO_List, pk=pk)
    if request.method == 'GET':
        form = ToDoForm(initial={
            'status': todo_action.status,
            'description': todo_action.description,
            'long_description': todo_action.long_description,
            'deadline': todo_action.deadline
            })
        return render(request, 'update_to_do_action.html', context={'form': form,
                                                                    'todo_action': todo_action})
    elif request.method == 'POST':
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            todo_action.status = form.cleaned_data['status']
            todo_action.description = form.cleaned_data['description']
            todo_action.long_description = form.cleaned_data['long_description']
            todo_action.deadline = form.cleaned_data['deadline']
            todo_action.save()
            return redirect('watch_todo', pk=todo_action.pk)
        else:
            return render(request, 'update_to_do_action.html', context={'form': form,
                                                                        'todo_action': todo_action})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])