from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from home.models import Mesaj
from home.forms import MesajForm
from Floris_Dent.settings import EMAIL_HOST_USER


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
    success_url = reverse_lazy('create-mesaj')
