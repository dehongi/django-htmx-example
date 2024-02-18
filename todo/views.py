from django.shortcuts import render
from django.urls import reverse

from django.views import generic

from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 10


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
