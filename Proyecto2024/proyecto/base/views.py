"""docstring"""
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea

class ListaPendientes(ListView):
    """docstring"""
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    """docstring"""
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'
