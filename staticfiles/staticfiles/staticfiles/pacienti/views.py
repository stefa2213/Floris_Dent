from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from pacienti.filters import PreturiFilter
from pacienti.forms import PacientForm
from pacienti.models import Pacient


class PacientiCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pacienti/create_pacienti.html'
    model = Pacient
    form_class = PacientForm
    success_url = reverse_lazy('list-of-pacienti')


class PacientiListView(LoginRequiredMixin, ListView):
    template_name = 'pacienti/list_of_pacienti.html'
    model = Pacient
    context_object_name = 'all_pacienti'

    def get_context_data(self, **kwargs):
        data = super(PacientiListView, self).get_context_data(**kwargs)

        all_pacienti = Pacient.objects.all()

        data['pacienti'] = all_pacienti

        my_filter_ = PreturiFilter(self.request.GET, queryset=all_pacienti.order_by('nume'))
        data['all_pacienti'] = my_filter_.qs
        data['my_filter'] = my_filter_

        return data


class PacientiDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pacienti/detail_pacienti.html'
    model = Pacient


class PacientiUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pacienti/update_pacienti.html'
    model = Pacient
    form_class = PacientForm
    success_url = reverse_lazy('list-of-pacienti')


@permission_required('pacient.delete_pacient')
def delete_pacient(request, pk):
    Pacient.objects.filter(id=pk).delete()
    return redirect('list-of-pacienti')
