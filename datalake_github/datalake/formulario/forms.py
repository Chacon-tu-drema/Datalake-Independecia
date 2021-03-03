from django import forms
from .models import FormularioBase

class FormularioBase(forms.ModelForm):

    class Meta:
        model = FormularioBase
        fields = [
            'p_origen',
            'tipo_identificacion',
            'numero_identificacion',
            'direccion',
            'numero_calle',
            'texto1',
            'texto2',
            'texto3',
            'texto4',
            'autor'
            ]
