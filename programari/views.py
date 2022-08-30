import requests
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from Floris_Dent.settings import EMAIL_HOST_USER
from programari.filters import ProgramariFilters
from programari.forms import ProgramariForm
from programari.models import Programari


class ProgramariCreateView(CreateView):
    template_name = 'programari/create_programare.html'
    model = Programari
    form_class = ProgramariForm
    success_url = reverse_lazy('create-programare')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            noua_programare = form.save()
            subject = 'O noua programare la FlorisDent'

            message = None
            my_html_message = render_to_string('email/email_programare.html', {'details_user': noua_programare})
            my_html_message_doctor = render_to_string('email/email_programare_doctor.html',
                                                      {'details_user': noua_programare})
            send_mail(subject, message, EMAIL_HOST_USER,
                      [noua_programare.email],
                      html_message=my_html_message)  # folosim lista la email chiar daca e unul singur
            send_mail(subject, message, EMAIL_HOST_USER, [noua_programare.doctor.email],
                      html_message=my_html_message_doctor)

            return redirect('locatie')


class ProgramareListView(ListView):
    template_name = 'programari/list_of_programari.html'
    model = Programari
    context_object_name = 'all_programari'

    def get_context_data(self, **kwargs):
        data = super(ProgramareListView, self).get_context_data(**kwargs)

        all_programari = Programari.objects.all()
        data['programari'] = all_programari

        my_filter_ = ProgramariFilters(self.request.GET, queryset=all_programari)
        data['all_programari'] = my_filter_.qs
        data['my_filter'] = my_filter_

        return data


class ProgramareListViewAnulate(ListView):
    template_name = 'programari/list_of_programari_anulate.html'
    model = Programari
    context_object_name = 'all_programari_anulate'

    def get_context_data(self, **kwargs):
        data = super(ProgramareListViewAnulate, self).get_context_data(**kwargs)

        all_programari_anulate = Programari.objects.filter(active=False)
        data['programari_anulate'] = all_programari_anulate

        my_filter_ = ProgramariFilters(self.request.GET, queryset=all_programari_anulate)
        data['all_programari_anulate'] = my_filter_.qs
        data['my_filter_anulate'] = my_filter_

        return data


class ProgramariUpdateView(UpdateView):
    template_name = 'programari/update_programare.html'
    model = Programari
    form_class = ProgramariForm
    success_url = reverse_lazy('list-of-programari')

    # permission_required = 'doctor.change_programari'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            noua_programare = form.save()
            subject = 'O noua programare la FlorisDent'

            message = None
            my_html_message = render_to_string('email/email_programare_update.html', {'details_user': noua_programare})
            my_html_message_doctor = render_to_string('email/email_programare_doctor_update.html',
                                                      {'details_user': noua_programare})
            send_mail(subject, message, EMAIL_HOST_USER,
                      [noua_programare.email],
                      html_message=my_html_message)
            send_mail(subject, message, EMAIL_HOST_USER, [noua_programare.doctor.email],
                      html_message=my_html_message_doctor)

            return redirect('list-of-programari')


def delete_programare(request, pk):
    Programari.objects.filter(id=pk).delete()
    return redirect('list-of-programari-anulate')


def inactive_programare(request, pk):
    Programari.objects.filter(id=pk).update(active=False)
    return redirect('list-of-programari')


def active_programare(request, pk):
    Programari.objects.filter(id=pk).update(active=True)
    return redirect('list-of-programari')
