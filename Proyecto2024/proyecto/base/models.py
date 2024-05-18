"""docstring"""
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    """docstring"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.titulo
    
    class Meta:
        """docstring"""
        ordering = ['completo']
