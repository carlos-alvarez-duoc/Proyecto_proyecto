from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, logueo,Logout

urlpatterns = [
    path('', ListaPendientes.as_view(), name='lista-pendientes'),
    path('login/', logueo.as_view(), name='login'),
    path('logout/', Logout.as_view(next_page= 'login'), name='logout'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle-tarea'),
    path('tarea/nueva/', CrearTarea.as_view(), name='crear-tarea'),
    path('tarea/<int:pk>/editar/', EditarTarea.as_view(), name='editar-tarea'),
    path('tarea/<int:pk>/eliminar/', EliminarTarea.as_view(), name='eliminar-tarea'),
    
  
]