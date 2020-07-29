from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import TO_DO_List
from webapp.forms import ToDoForm


def index_view(request):
    if request.method == 'GET':
        to_do_list = TO_DO_List.objects.all()
        context = {
            'to_do_list': to_do_list
        }
        return render(request, 'index.html', context)


def delete_todo_action(request, pk):
    todo_action = get_object_or_404(TO_DO_List, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo_action': todo_action})
    elif request.method == 'POST':
        todo_action.delete()
        return redirect('index_view')


def create_todo_action(request):
    if request.method == 'GET':
        return render(request, 'create_todo_action.html', context={
            'form': ToDoForm()
        })
    elif request.method == 'POST':
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            to_do_action = TO_DO_List.objects.create(
                status=form.cleaned_data['status'],
                description=form.cleaned_data['description'],
                long_description=form.cleaned_data['long_description'],
                deadline=form.cleaned_data['deadline']
            )
            return redirect('watch_todo', to_do_action.pk)
        else:
            return render(request,'create_todo_action.html', context={
                'form': form
            })


def watch_todo(request, pk):
    to_do_action = TO_DO_List.objects.get(pk=pk)
    context = {
        'to_do_action': to_do_action
    }
    return render(request, 'view_to_do_action.html', context)


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