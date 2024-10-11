from django import forms
from .models import Evolucao

class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['paciente', 'data_sessao', 'observacoes']
        widgets = {
            'data_sessao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 4}),
        }