from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Note(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    texto = RichTextField(verbose_name='Nota')
    nemotecnico = models.CharField(max_length=50, verbose_name='Nemotécnico')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.nombre

