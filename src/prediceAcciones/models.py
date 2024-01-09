from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Accion(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=128)
    identificador = models.CharField(max_length=20)

    def __str__(self):
        return self.identificador

class HistoricoAccion(models.Model):
    accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return self.valor
    
