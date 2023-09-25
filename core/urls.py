from django.urls import path
from .views import TaskListView, TaskListDetail, TaskDetail, CreateListView, change_status_view, task_update_view, delete_task_view, ListDeleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('create/', CreateListView.as_view(), name='create'),
    path('update/<int:pk>/', task_update_view, name='update'),
    path('delete/<int:pk>/', delete_task_view, name='delete_task'),
    path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='delete_list'),
    path('list/detail/<int:pk>/', TaskListDetail.as_view(), name='list'),
    path('task/detail/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/changestatus/<int:pk>/', change_status_view, name='changestatus'),
]
