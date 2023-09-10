from django.urls import path
from .views import TaskListView, create_list_with_tasks

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('create/', create_list_with_tasks, name='create')
]
