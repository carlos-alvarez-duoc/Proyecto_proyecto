"""docstring"""
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea

class ListaPendientes(ListView):
    model = Tarea