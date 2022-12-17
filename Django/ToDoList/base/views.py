from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


# Create your views here.

class TaskList(ListView):
    #return HttpResponse("To Do List") 
    model = Task
    context_object_name = 'TaskList'
    template_name = 'base/task.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'TaskDetail'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('TaskList')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('TaskList')

class TaskDelete(DeleteView):
    model = Task
    content_object_name = 'TaskDelete'
    success_url = reverse_lazy('TaskList')
    