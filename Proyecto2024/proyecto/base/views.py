from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Tarea
from django.views.generic import TemplateView

class logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tareas')

class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'base/tareas.html'

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'

class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')

class Logout(LogoutView):
    template_name = 'base/logout.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'

    