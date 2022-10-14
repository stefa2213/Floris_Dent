from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from pacienti.models import Pacient


class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['nume', 'varsta', 'telefon', 'email', 'detalii']

        widgets = {
            'nume': TextInput(attrs={'placeholder': 'Introduceți numele...(obligatoriu)', 'class': 'form-control'}),
            'varsta': TextInput(attrs={'placeholder': 'Introduceți vârsta...', 'class': 'form-control'}),
            'telefon': TextInput(attrs={'placeholder': 'Introduceți numarul de telefon...', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Introduceți adresa de email...', 'class': 'form-control'}),
            'detalii': Textarea(
                attrs={'placeholder': 'Introduceți detalii despre pacient...', 'class': 'form-control'}),
        }
