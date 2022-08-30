from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from home.models import Mesaj


class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['nume', 'email', 'numar_telefon', 'subiect', 'mesaj']

        widgets = {
            'nume': TextInput(attrs={'placeholder': 'Numele dumneavoastra', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Adresa  de email', 'class': 'form-control'}),
            'numar_telefon': TextInput(
                attrs={'placeholder': 'Numarul de telefon (optional) ', 'class': 'form-control'}),
            'subiect': TextInput(attrs={'placeholder': 'Subiectul mesajului', 'class': 'form-control'}),
            'mesaj': Textarea(attrs={'placeholder': 'Scrieti mesajul dorit', 'class': 'form-control'})
        }
