from django.contrib import admin
from .models import FormularioBase, CallesCondiciones, Paises

class FormularioBaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class CallesCondicionesAdmin(admin.ModelAdmin):
    readonly_fields = ('calle','condiciones')

class PaisesAdmin(admin.ModelAdmin):
    readonly_fields = ['nombre']

admin.site.register(FormularioBase,FormularioBaseAdmin)
admin.site.register(CallesCondiciones,CallesCondicionesAdmin)
admin.site.register(Paises,PaisesAdmin)


