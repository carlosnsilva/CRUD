from django import forms
from .models import agenda

class Insertagenda(forms.ModelForm):

    class Meta:
        model = agenda

        fields = [
            'nome',
            'fone',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'email',
            'sexo',
            'data'
        ]