import django_filters
from django import forms

from home.models import Mesaj


class MesajeFilters(django_filters.FilterSet):
    nume = django_filters.CharFilter(lookup_expr='icontains', label='Nume')
    numar_telefon = django_filters.CharFilter(lookup_expr='icontains', label='Numar Telefon')
    subiect = django_filters.CharFilter(lookup_expr='icontains', label='Subiect')

    class Meta:
        model = Mesaj
        fields = ['nume', 'numar_telefon', 'subiect']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['nume'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Cautati dupa nume'})
        self.filters['numar_telefon'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Cautati dupa numar de telefon'})
        self.filters['subiect'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Cautati dupa subiect'})