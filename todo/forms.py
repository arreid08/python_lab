from django import forms
from .models import Group, Task

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('group_name',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_name', 'notes',)
