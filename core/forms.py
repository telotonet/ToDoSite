from django import forms

class TaskForm(forms.Form):
    list_name = forms.CharField(max_length=255, required=True, label='Название списка задач')
    tasks = forms.CharField(widget=forms.Textarea, required=False, label='Задачи')
