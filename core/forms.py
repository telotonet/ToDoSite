from django import forms
from .models import List, Task

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg mb-3'
        self.fields['title'].widget.attrs['placeholder'] = 'Введите название списка'

        self.fields['title'].initial = None

from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Введите название задачи'

        self.fields['title'].initial = None
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['rows'] = '3'

        self.fields['status'].widget.attrs['class'] = 'form-check-input'

        # self.fields['due_at'].widget.attrs['class'] = 'form-control'


