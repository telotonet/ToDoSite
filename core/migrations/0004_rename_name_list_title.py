# Generated by Django 4.2.5 on 2023-09-15 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_task_task_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='name',
            new_name='title',
        ),
    ]
