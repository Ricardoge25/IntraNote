from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Incident(models.Model):
    id_servicio = models.CharField(max_length=20, verbose_name='Identificador', unique=True)
    nombre_anillo = models.CharField(max_length=20, verbose_name='Anillo')
    nombre_cliente = models.CharField(max_length=50, verbose_name='Empresa')
    nit = models.CharField(max_length=15, verbose_name='Nit')   
    nombre_contacto = models.CharField(max_length=30, verbose_name='Nombre contacto')
    numero_contacto = models.CharField(max_length=15, verbose_name='Número contacto')
    correo_contacto = models.EmailField(verbose_name='Correo contacto')
    direccion_servicio = models.CharField(max_length=50, verbose_name='Dirección servicio')
    ip = models.CharField(max_length=16, verbose_name='ip switch')
    observaciones = models.TextField(verbose_name='Observaciones',  blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidentes', null=True)

    class Meta:
        verbose_name = 'incidente'
        verbose_name_plural = 'incidentes'
        ordering = ["-created"]

    def __str__(self):
        return self.id_servicio
