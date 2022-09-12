from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from preturi.filters import PretFilter
from preturi.forms import PretForm
from preturi.models import Pret


class PreturiCreateView(LoginRequiredMixin, CreateView):
    template_name = 'preturi/create_preturi.html'
    model = Pret
    form_class = PretForm
    success_url = reverse_lazy('create-preturi')


class PreturiListView(ListView):
    template_name = 'preturi/list_preturi.html'
    model = Pret
    context_object_name = 'all_preturi'

    def get_context_data(self, **kwargs):
        data = super(PreturiListView, self).get_context_data(**kwargs)

        all_preturi = Pret.objects.all()
        data['preturi'] = all_preturi

        my_filter_ = PretFilter(self.request.GET, queryset=all_preturi)
        data['all_preturi'] = my_filter_.qs
        data['my_filter'] = my_filter_

        return data


class PreturiListViewAnulate(LoginRequiredMixin, ListView):
    template_name = 'preturi/list_preturi_dezactivate.html'
    model = Pret
    context_object_name = 'all_preturi_anulate'

    def get_context_data(self, **kwargs):
        data = super(PreturiListViewAnulate, self).get_context_data(**kwargs)

        all_preturi_anulate = Pret.objects.filter(active=False)
        data['preturi_anulate'] = all_preturi_anulate

        my_filter_ = PretFilter(self.request.GET, queryset=all_preturi_anulate)
        data['all_preturi_anulate'] = my_filter_.qs
        data['my_filter_anulate'] = my_filter_

        return data


class PreturiUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'preturi/update_preturi.html'
    model = Pret
    form_class = PretForm
    success_url = reverse_lazy('list-preturi')


@permission_required('pret.delete_pret')
def delete_serviciu(request, pk):
    Pret.objects.filter(id=pk).delete()
    return redirect('list-preturi')


@permission_required('pret.change_pret')
def deactivate_pret(request, pk):
    Pret.objects.filter(id=pk).update(active=False)
    return redirect('list-preturi')


@permission_required('pret.change_pret')
def activate_pret(request, pk):
    Pret.objects.filter(id=pk).update(active=True)
    return redirect('list-preturi')
