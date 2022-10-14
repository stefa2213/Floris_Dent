import django_filters
from django import forms

from programari.models import Programari


class ProgramariFilters(django_filters.FilterSet):
    prenume = django_filters.CharFilter(lookup_expr='icontains', label='Prenume')
    nume = django_filters.CharFilter(lookup_expr='icontains', label='Nume')
    varsta_gte = django_filters.CharFilter(field_name='varsta', lookup_expr='gte', label='Varsta - de la:',
                                           widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control',
                                                                         'placeholder': 'Introduceti varsta minima'}))
    varsta_lte = django_filters.CharFilter(field_name='varsta', lookup_expr='lte', label='Varsta - pana la:',
                                           widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control',
                                                                         'placeholder': 'Introduceti varsta maxima'}))
    numar_telefon = django_filters.CharFilter(lookup_expr='icontains', label='Numar Telefon')
    ora_programare_gte = django_filters.DateTimeFilter(field_name='ora_programare', lookup_expr='gte',
                                                       label='Ora programare - de la:', widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'}))
    ora_programare_lte = django_filters.DateTimeFilter(field_name='ora_programare', lookup_expr='lte',
                                                       label='Ora programare - pana la:', widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'}))

    class Meta:
        model = Programari
        fields = ['prenume', 'nume', 'varsta_gte', 'varsta_lte', 'numar_telefon', 'ora_programare_gte',
                  'ora_programare_lte', 'doctor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['prenume'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceti prenumele pacientului'})
        self.filters['nume'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceti numele pacientului'})
        self.filters['numar_telefon'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceti numarul de telefon'})
        self.filters['doctor'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introduceti adresa de email'})
