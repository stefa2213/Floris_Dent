import django_filters
from django import forms

from preturi.models import Pret


class PretFilter(django_filters.FilterSet):
    nume_serviciu = django_filters.CharFilter(lookup_expr='icontains', label='Nume serviciu')
    pret_gte = django_filters.CharFilter(field_name='pret_serviciu', lookup_expr='gte', label='Pret - de la:',
                                         widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control'}))
    pret_lte = django_filters.CharFilter(field_name='pret_serviciu', lookup_expr='lte', label='Pret - pana la:',
                                         widget=forms.DateInput(attrs={'type': 'number', 'class': 'form-control'}))
    detalii = django_filters.CharFilter(lookup_expr='icontains', label='Detalii serviciu')

    class Meta:
        model = Pret
        fields = ['nume_serviciu', 'pret_gte', 'pret_lte', 'detalii']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['nume_serviciu'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Introdu numele serviciului'})
        self.filters['detalii'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Detalii'})
