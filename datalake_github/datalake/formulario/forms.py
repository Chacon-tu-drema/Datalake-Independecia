from django import forms
from .models import FormularioBase

class FormularioBase(forms.ModelForm):

    class Meta:
        model = FormularioBase
        fields = ['rut']
