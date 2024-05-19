from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks
from .forms import TasksForm, TasksEditForm

class TaskView(LoginRequiredMixin, ListView):
    model = Tasks
    paginate_by = 10
    ordering='-start_date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')  # Redirect to the list of tasks after saving
    else:
        form = TasksForm()

    return render(request, 'create_task.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TasksEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')  # Redirect to the list of tasks after saving
    else:
        form = TasksEditForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list_tasks')
    return render(request, 'delete_task.html', {'task': task})
