from django.shortcuts import render
from webapp.models import TO_DO_List


def index_view(reqest):
    to_do_list = TO_DO_List.objects.all()
    context = {
        'to_do_list': to_do_list
    }
    return render(reqest, 'index.html', context)
