import django_filters
from django import forms

from pacienti.models import Pacient


class PreturiFilter(django_filters.FilterSet):
    nume = django_filters.CharFilter(lookup_expr='icontains', label='Nume')
    varsta_gte = django_filters.CharFilter(field_name='varsta', lookup_expr='gte', label='Varsta - de la:',
                                           widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control',
                                                                         'placeholder': 'Introduceți varsta minimă'}))
    varsta_lte = django_filters.CharFilter(field_name='varsta', lookup_expr='lte', label='Varsta - pana la:',
                                           widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control',
                                                                         'placeholder': 'Introduceți varsta maximă'}))
    telefon = django_filters.CharFilter(lookup_expr='icontains', label='Număr Telefon')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Adresă Email')

    class Meta:
        model = Pacient
        fields = ['nume', 'varsta_gte', 'varsta_lte', 'telefon', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['nume'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceți numele...'})
        self.filters['telefon'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceți numarul de telefon'})
        self.filters['email'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceți adresa de email'})
