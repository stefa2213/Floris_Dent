import datetime
import smtplib
import os

from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, get_connection
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from Floris_Dent.settings import EMAIL_HOST_USER
from programari.filters import ProgramariFilters
from programari.forms import ProgramariForm
from programari.models import Programari


class ProgramariCreateView(CreateView):
    template_name = 'programari/create_programare.html'
    model = Programari
    form_class = ProgramariForm
    success_url = reverse_lazy('programare-succes')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            noua_programare = form.save()
            subject = 'O noua programare la FlorisDent'

            message = None
            my_html_message = render_to_string('email/email_programare.html', {'details_user': noua_programare})
            my_html_message_doctor = render_to_string('email/email_programare_doctor.html',
                                                      {'details_user': noua_programare})
            send_mail(subject, message, EMAIL_HOST_USER, [noua_programare.email],html_message=my_html_message)  # folosim lista la email chiar daca e unul singur
            send_mail(subject, message, EMAIL_HOST_USER, [noua_programare.doctor.email],
                      html_message=my_html_message_doctor)

            return redirect('locatie')


class ProgramareListView(LoginRequiredMixin, ListView):
    template_name = 'programari/list_of_programari.html'
    model = Programari
    context_object_name = 'all_programari'

    def get_context_data(self, **kwargs):
        data = super(ProgramareListView, self).get_context_data(**kwargs)

        all_programari = Programari.objects.all()

        for programare in all_programari:
            if programare.ora_programare < timezone.make_aware(datetime.datetime.now(),
                                                               timezone.get_default_timezone()):
                programare.active = False
                programare.save()

        data['programari'] = all_programari

        my_filter_ = ProgramariFilters(self.request.GET, queryset=all_programari.order_by('ora_programare'))
        data['all_programari'] = my_filter_.qs
        data['my_filter'] = my_filter_

        return data


class ProgramareListViewAnulate(LoginRequiredMixin, ListView):
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


class ProgramariDetailView(LoginRequiredMixin, DetailView):
    template_name = 'programari/detail_programari.html'
    model = Programari


class ProgramariUpdateView(LoginRequiredMixin, UpdateView):
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


@permission_required('programari.delete_programari')
def delete_programare(request, pk):
    Programari.objects.filter(id=pk).delete()
    return redirect('list-of-programari-anulate')


@permission_required('programari.change_programari')
def inactive_programare(request, pk):
    Programari.objects.filter(id=pk).update(active=False)
    return redirect('list-of-programari')


@permission_required('programari.change_programari')
def active_programare(request, pk):
    Programari.objects.filter(id=pk).update(active=True)
    return redirect('list-of-programari')
