from django.shortcuts import render
from webapp.models import TO_DO_List


def index_view(request):
    if request.method == 'GET':
        to_do_list = TO_DO_List.objects.all()
        context = {
            'to_do_list': to_do_list
        }
        return render(request, 'index.html', context)


def delete_todo_action(request):
    to_do_action_id = request.POST.get('id')
    to_do_action = TO_DO_List.objects.get(pk=to_do_action_id)
    to_do_action.delete()
    to_do_list = TO_DO_List.objects.all()
    context = {
        'to_do_list': to_do_list
    }
    return render(request, 'index.html', context)


def create_todo_action(request):
    if request.method == 'GET':
        status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
        context = {
            'Statuses': status_choices
        }
        return render(request, 'create_todo_action.html', context)
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date') or None
        to_do_action = TO_DO_List.objects.create(description=description, status=status, deadline=date)
        context = {
            'to_do_action': to_do_action
        }
        return render(request, 'view_to_do_action.html', context)
