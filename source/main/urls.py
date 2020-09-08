"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import IndexView,CreateTodoView, DeleteTodoView, WatchTodoView, UpdateTodoView, Project_view, \
    Watch_project_view, Create_project_view,ProjectToDoCreateView, ProjectUpdateView, ProjectDeleteView, ManageTeamView
from django.contrib.auth.views import LogoutView, LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_view'),
    path('add/', CreateTodoView.as_view(), name='add'),
    path('todo/<int:pk>/', WatchTodoView.as_view(), name='watch_todo'),
    path('todo/<int:pk>/delete/', DeleteTodoView.as_view(), name='delete_todo'),
    path('todo/<int:pk>/update/', UpdateTodoView.as_view(), name='update_todo'),

    path('projects/', Project_view.as_view(), name='projects'),
    path('projects/<int:pk>/', Watch_project_view.as_view(), name='watch_project'),
    path('projects/add/', Create_project_view.as_view(), name='add project'),
    path('projects/<int:pk>/to_do_action/add/', ProjectToDoCreateView.as_view(),
         name='project_todo_add'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/manage_team/', ManageTeamView.as_view(), name='manage_team'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),

    path('accounts/', include('accounts.urls')),

]
