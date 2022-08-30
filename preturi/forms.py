from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from preturi.models import Pret


class PretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ['nume_serviciu', 'pret_serviciu', 'detalii', 'durata']

        widgets = {
            'nume_serviciu': TextInput(
                attrs={'placeholder': 'Introduceti numele serviciului...(camp obligatoriu)', 'class': 'form-control'}),
            'pret_serviciu': TextInput(
                attrs={'placeholder': 'Introduceti pretul serviciului... (camp obligatoriu)', 'class': 'form-control'}),
            'detalii': Textarea(
                attrs={'placeholder': 'Introduceti detalii despre serviciu...', 'class': 'form-control'}),
            'durata': TextInput(attrs={'placeholder': 'Durata aproximativa a serviciului in minute...(camp obligatoriu)',
                                       'class': 'form-control', 'type': 'number'})
        }
