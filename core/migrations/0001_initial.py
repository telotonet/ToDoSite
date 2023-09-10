# Generated by Django 4.2.5 on 2023-09-09 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Список без названия', max_length=255, null=True, verbose_name='Список задач')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Задача без названия', max_length=255, null=True, verbose_name='Задача')),
                ('description', models.TextField(blank=True, verbose_name='Задача')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('due_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('status', models.BooleanField(default=False, verbose_name='Статус выполнения')),
                ('parent_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='core.task', verbose_name='Родительская задача')),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.list', verbose_name='Список задач')),
            ],
        ),
    ]
