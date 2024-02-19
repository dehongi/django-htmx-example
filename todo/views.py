from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from django.views import generic

from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(completed=False)


def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    # Optionally, you can return a JSON response indicating success
    return JsonResponse({"message": "Task marked as completed successfully"})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self) -> str:
        return reverse("task_list")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
