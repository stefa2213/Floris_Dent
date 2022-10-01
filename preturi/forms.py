from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from preturi.models import Pret


class PretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ['nume_serviciu', 'pret_serviciu', 'detalii', 'durata']

        widgets = {
            'nume_serviciu': TextInput(
                attrs={'placeholder': 'Introduceți numele serviciului...(obligatoriu)', 'class': 'form-control'}),
            'pret_serviciu': TextInput(
                attrs={'placeholder': 'Introduceți pretul serviciului... (obligatoriu)', 'class': 'form-control'}),
            'detalii': Textarea(
                attrs={'placeholder': 'Introduceți detalii despre serviciu...', 'class': 'form-control'}),
            'durata': TextInput(attrs={'placeholder': 'Durata aproximativă a serviciului în minute...(obligatoriu)',
                                       'class': 'form-control', 'type': 'number'})
        }
