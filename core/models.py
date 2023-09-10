from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class List(models.Model):
    name = models.CharField(max_length=255, default='Список без названия', verbose_name='Список задач', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('list', kwargs={'id':self.id})
    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'

class Task(models.Model):
    title = models.CharField(max_length=255, default='Задача без названия', verbose_name='Задача', blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Задача')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    due_at  = models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')
    # category = models.CharField(max_length=255, blank=True, verbose_name='Категория')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Категория')
    status = models.BooleanField(default=False, verbose_name='Статус выполнения')
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_tasks', verbose_name='Родительская задача')
    task_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks',verbose_name='Список задач', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('task', kwargs={'id':self.id})
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'