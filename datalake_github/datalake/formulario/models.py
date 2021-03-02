from django.db import models
from django.contrib.auth.models import User

class Paises(models.Model): 
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class CallesCondiciones(models.Model):
    calle = models.CharField(max_length=30)
    condiciones = models.TextField()

    class Meta:
        verbose_name = "Calle y UV"
        verbose_name_plural = "Calles y UV"
        ordering = ['calle']
        
    def __str__(self):
        return f'{self.calle}'

class FormularioBase(models.Model):
    p_origen = models.CharField(default="", max_length=30, verbose_name="Pais de Origen")
    tipo_identificacion = models.CharField(default="", max_length=30,
                                            choices=(
                                                ('Rut','Rut'),
                                                ('Pasaporte','Pasaporte'),
                                                ('Otro','Otro'),
                                            )
                                          )
    numero_identificacion = models.CharField(default="", max_length=30)
    direccion = models.CharField(default="", max_length=30)
    numero_casa = models.PositiveIntegerField(default=0)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento") 
    texto1 = models.TextField(blank=True, verbose_name="Texto 1")
    texto2 = models.TextField(blank=True, verbose_name="Texto 2")
    texto3 = models.TextField(blank=True, verbose_name="Texto 3")
    texto4 = models.TextField(blank=True, verbose_name="Texto 4")

    autor = models.ForeignKey(User, on_delete=models.PROTECT)  
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", editable=False) 

    class Meta:
        verbose_name = "formulario base"
        verbose_name_plural = "formularios bases"
        ordering = ['-created']

  
    def __str__(self):
        return f'{self.created} - {self.rut} '
    