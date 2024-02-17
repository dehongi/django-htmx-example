from django.shortcuts import render

from django.views import generic

from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
