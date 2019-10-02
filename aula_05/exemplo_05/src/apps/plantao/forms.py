from django import forms
from .models import Plantonista


class PlantonistaForm(forms.ModelForm):
    class Meta:
        model = Plantonista
        fields = [
            'id',
            'área',
            'nome',
            'telefone',
            'observação'
        ]
