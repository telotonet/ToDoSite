from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task, List
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm

class TaskListView(ListView, LoginRequiredMixin):
    model = List
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self) -> QuerySet[Any]:
        return List.objects.filter(user=self.request.user)

def create_list_with_tasks(request):
    if request.method == 'POST':
        list_name = request.POST.get('list_name')
        tasks = request.POST.getlist('tasks[]')

        new_list = List(name=list_name, user=request.user)
        new_list.save()

        for i, task_text in enumerate(tasks):
            task_text = task_text.strip()
            if task_text:
                task = Task(title=task_text, task_list=new_list, user=request.user)
                task.save()

                subtasks = request.POST.getlist(f'subtasks[{i}][]')
                for subtask_text in subtasks:
                    subtask_text = subtask_text.strip()
                    if subtask_text:
                        subtask = Task(title=subtask_text, parent_task=task, user=request.user)
                        subtask.save()

    return render(request, 'create_list.html')


