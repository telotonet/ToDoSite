from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, DeleteView
from .models import Task, List
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ListForm, TaskForm
from django.forms import modelformset_factory
from django.http import Http404
# from .forms import TaskForm

def change_status_view(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if task_obj.user == request.user:
        task_obj.status=True
        task_obj.save() 
        return redirect(task_obj.get_absolute_url())
    return redirect('tasks')

class TaskListDetail(LoginRequiredMixin, DetailView):
    model = List
    login_url = reverse_lazy('login')
    template_name = 'list_detail.html'
    context_object_name = 'list'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return List.objects.filter(user=self.request.user).prefetch_related('tasks', 'tasks__sub_tasks')

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    login_url = reverse_lazy('login')
    template_name = 'task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).prefetch_related('sub_tasks')

class TaskListView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'task_list.html'
    context_object_name = 'lists'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return List.objects.filter(user=self.request.user).prefetch_related('tasks')


class CreateListView(TemplateView):
    template_name = 'list_create.html'
    TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=0, can_delete=True, can_delete_extra=True)
    def get(self, request, *args, **kwargs):

        list_form = ListForm()
        task_formset = self.TaskFormSet(queryset=Task.objects.none())
        return render(request, self.template_name, {'list_form': list_form, 'task_formset': task_formset})

    def post(self, request, *args, **kwargs):
        list_form = ListForm(request.POST)
        task_formset = self.TaskFormSet(request.POST)
        if list_form.is_valid() and task_formset.is_valid():
            new_list = list_form.save(commit=False)
            new_list.user = request.user
            new_list.save()

            for task_form in task_formset:
                if not task_form.cleaned_data.get('DELETE', False):
                    task = task_form.save(commit=False)
                    task.task_list = new_list
                    task.user = request.user
                    task.save()

            return redirect(new_list.get_absolute_url())
        return render(request, self.template_name, {'list_form': list_form, 'task_formset': task_formset})


def task_update_view(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.user == request.user:
        return redirect('tasks')
    TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        formset = TaskFormSet(request.POST, queryset=Task.objects.filter(parent_task=task))
        if form.is_valid() and formset.is_valid():
            form.save()
            for task_form in formset:
                if not task_form.cleaned_data.get('DELETE', False):
                    new_task = task_form.save(commit=False)
                    new_task.parent_task = task
                    new_task.user = request.user
                    new_task.save()
            return redirect(task.get_absolute_url())
    else:
        form = TaskForm(instance=task)
        formset = TaskFormSet(queryset=Task.objects.filter(parent_task=task))

    context = {
        'form': form,
        'formset': formset,
        'task': task,
    }
    return render(request, 'task_update.html', context)

def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    redirect_url = reverse('tasks')
    if task.user == request.user:
        if task.parent_task != None:
            redirect_url = reverse('task', kwargs={'pk':task.parent_task.pk, })
        elif task.task_list != None:
            redirect_url = reverse('list', kwargs={'pk':task.task_list.pk, })
        task.delete()
    return redirect(redirect_url)

class ListDeleteView(DeleteView):
    model = List
    template_name = 'list_confirm_delete.html'
    success_url = reverse_lazy('tasks')

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise Http404
        return task