from django.contrib import admin
from .models import FormularioBase, Direccion

class DireccionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class FormularioBaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(FormularioBase,FormularioBaseAdmin)
admin.site.register(Direccion,DireccionAdmin)

