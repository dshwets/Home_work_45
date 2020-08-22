from django.contrib import admin
from webapp.models import TO_DO_List,Statuses,Issues,Project

admin.site.register(TO_DO_List)
admin.site.register(Statuses)
admin.site.register(Issues)
admin.site.register(Project)