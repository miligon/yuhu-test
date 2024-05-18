from django.shortcuts import get_object_or_404, render
from .models import Tasks

# Create your views here.
def list_tasks(request):
    tareas = Tasks.objects.all()
    context = {
        'tareas' : tareas
    }
    return render(request, "list.html", context)

def main(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm

def create_task(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')  # Redirect to the list of tasks after saving
    else:
        form = TasksForm()

    return render(request, 'create_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')  # Redirect to the list of tasks after saving
    else:
        form = TasksForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})
