from django.db import models
from datetime import date, datetime
# Create your models here.

class Gastos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=False)
    descripcion = models.CharField(max_length=100,null=True)
    valor = models.FloatField()
    fecha = models.DateField()
    categoria = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.nombre
