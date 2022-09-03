from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from home.models import Mesaj
from home.forms import MesajForm
from django.shortcuts import render, redirect
from home.filters import MesajeFilters
from Floris_Dent.settings import EMAIL_HOST_USER
from django.contrib import messages


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


class LocationTemplateView(TemplateView):
    template_name = 'home/locatie.html'


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'


class MesajCreateView(CreateView):
    template_name = 'home/contact.html'
    model = Mesaj
    form_class = MesajForm
    success_url = reverse_lazy('create-mesaj-succes')


class MesajDetailView(DetailView):
    template_name = 'home/detail_mesaj.html'
    model = Mesaj


class MesajListView(ListView):
    template_name = 'home/list_of_mesaje.html'
    model = Mesaj
    context_object_name = 'all_mesaje'

    def get_context_data(self, **kwargs):
        data = super(MesajListView, self).get_context_data(**kwargs)
        all_mesaje = Mesaj.objects.all()
        data['mesaje'] = all_mesaje

        my_filter_ = MesajeFilters(self.request.GET, queryset=all_mesaje.order_by('created_at'))
        data['all_mesaje'] = my_filter_.qs
        data['my_filter'] = my_filter_

        return data


class MesajListViewArhivate(ListView):
    template_name = 'home/list_of_mesaje_arhiva.html'
    model = Mesaj
    context_object_name = 'all_mesaje_arhivate'

    def get_context_data(self, **kwargs):
        data = super(MesajListViewArhivate, self).get_context_data(**kwargs)
        all_mesaje_arhivate = Mesaj.objects.filter(active=False)
        data['mesaje_arhivate'] = all_mesaje_arhivate

        my_filter_ = MesajeFilters(self.request.GET, queryset=all_mesaje_arhivate)
        data['all_mesaje_arhivate'] = my_filter_.qs
        data['my_filter_arhivate'] = my_filter_

        return data


class MsgSuccessTemplateView(TemplateView):
    template_name = 'home/create_mesaj_succes.html'


def rezolvare_mesaj(request, pk):
    Mesaj.objects.filter(id=pk).update(active=False)
    return redirect('list-of-mesaje')


def nerezolvare_mesaj(request, pk):
    Mesaj.objects.filter(id=pk).update(active=True)
    return redirect('list-of-mesaje')


def sterge_mesaj(request, pk):
    Mesaj.objects.filter(id=pk).delete()
    return redirect('list-of-mesaje-arhivate')
