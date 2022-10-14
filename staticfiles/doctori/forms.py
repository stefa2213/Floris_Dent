from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django import forms

from doctori.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nume_doctor', 'specializare', 'experienta', 'email', 'varsta', 'descriere', 'image']

        widgets = {
            'nume_doctor': TextInput(attrs={'placeholder': 'Introduceți numele complet', 'class': 'form-control'}),
            'specializare': TextInput(
                attrs={'placeholder': 'Introduceți specializarea dumneavoastră', 'class': 'form-control'}),
            'experienta': TextInput(
                attrs={'placeholder': 'Introduceți experiența în domeniul (ani)', 'class': 'form-control',
                       'type': 'number'}),
            'email': EmailInput(attrs={'placeholder': 'Introduceți adresa de email...', 'class': 'form-control'}),
            'varsta': TextInput(attrs={'placeholder': 'Introduceți vârsta', 'class': 'form-control', 'type': 'number'}),
            'descriere': Textarea(
                attrs={'placeholder': 'Scrieți câteva cuvinte despre dumneavoastră', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
