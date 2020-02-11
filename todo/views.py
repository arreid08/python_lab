from django.shortcuts import render, redirect

from .models import Group, Task
from .forms import GroupForm, TaskForm

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def group_detail(request, id):
    group = Group.objects.get(id = id)
    return render(request, 'group_detail.html', {'group': group})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid:
            group = form.save()
            return redirect('group_detail', id = group.id)
    else:
        form = GroupForm()
        return render(request, 'group_form.html', {'form': form})

def group_update(request, id):
    group = Group.objects.get(id = id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance = group)
        if form.is_valid:
            group = form.save()
            return redirect('group_detail', id = group.id)
    else:
        form = GroupForm(instance = group)
        return render(request, 'group_form.html', {'form': form})

def group_delete(request, id):
    Group.objects.get(id = id).delete()
    return redirect('group_list')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = Task.objects.get(id = id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save()
            return redirect('group_detail', id = task.group_id)
    else:
        form = TaskForm()
        return render(request, 'task_form.html', {'form': form})

def task_update(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid:
            task = form.save()
            return redirect('group_detail', id = task.group_id)
    else:
        form = TaskForm(instance = task)
        return render(request, 'task_form.html', {'form': form})

def task_delete(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('group_detail', id = task.group_id)
