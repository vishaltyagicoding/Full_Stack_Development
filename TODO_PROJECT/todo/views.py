from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        if not title:
            error = "Title is required."
            return render(request, 'task_form.html', {'error': error, 'title': title, 'description': description})
        
        Task.objects.create(title=title, description=description)
        return redirect('todo:task_list')
    return render(request, 'task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'
        
        if not title:
            error = "Title is required."
            return render(request, 'task_form.html', {'task': task, 'error': error})
        
        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        return redirect('todo:task_list')
    
    return render(request, 'task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
    
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('todo:task_list')