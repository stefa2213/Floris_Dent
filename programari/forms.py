from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from programari.models import Programari


class ProgramariForm(forms.ModelForm):
    class Meta:
        model = Programari
        fields = ['prenume', 'nume', 'varsta', 'numar_telefon', 'email', 'ora_programare', 'doctor']

        widgets = {
            'prenume': TextInput(attrs={'placeholder': 'Introduceti prenumele... (camp obligatoriu)', 'class': 'form-control'}),
            'nume': TextInput(attrs={'placeholder': 'Introduceti numele...(camp obligatoriu)', 'class': 'form-control'}),
            'varsta': TextInput(attrs={'placeholder': 'Introduceti varsta...(camp obligatoriu)', 'class': 'form-control'}),
            'numar_telefon': TextInput(attrs={'placeholder': 'Introduceti numarul de telefon...', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Introduceti adresa de email...', 'class': 'form-control'}),
            'ora_programare': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'doctor': Select(attrs={'class': 'form-control'})
        }
