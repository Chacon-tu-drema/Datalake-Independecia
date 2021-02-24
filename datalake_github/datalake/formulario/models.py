from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    direccion = models.CharField(max_length=20, verbose_name="Direccion")
    uv = models.PositiveSmallIntegerField(verbose_name="Unidad vecinal")
    numero = models.PositiveSmallIntegerField(verbose_name="Numero de casa")
    calle = models.CharField(max_length=30, verbose_name="Nombre de la calle")
    pc = models.PositiveIntegerField(verbose_name="Codigo Postal") 

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") 

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ['uv']
    
    def __str__(self):
        return f'{self.direccion}'

class FormularioBase(models.Model):
    rut = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    autor = models.ForeignKey(User, default='datalake', on_delete=models.SET_DEFAULT)  
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") 

    class Meta:
        verbose_name = "formulario base"
        verbose_name_plural = "formularios bases"
        ordering = ['-created']

  
    def __str__(self):
        return f'{self.rut} Formulario Base'
    