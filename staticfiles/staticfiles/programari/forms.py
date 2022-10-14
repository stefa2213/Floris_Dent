from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from programari.models import Programari


class ProgramariForm(forms.ModelForm):
    class Meta:
        model = Programari
        fields = ['prenume', 'nume', 'varsta', 'numar_telefon', 'email', 'ora_programare', 'doctor']

        widgets = {
            'prenume': TextInput(attrs={'placeholder': 'Introduceți prenumele... (obligatoriu)', 'class': 'form-control'}),
            'nume': TextInput(attrs={'placeholder': 'Introduceți numele...(obligatoriu)', 'class': 'form-control'}),
            'varsta': TextInput(attrs={'placeholder': 'Introduceți vârsta...(obligatoriu)', 'class': 'form-control'}),
            'numar_telefon': TextInput(attrs={'placeholder': 'Introduceți numarul de telefon...', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Introduceți adresa de email...', 'class': 'form-control'}),
            'ora_programare': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'doctor': Select(attrs={'class': 'form-control'})
        }
