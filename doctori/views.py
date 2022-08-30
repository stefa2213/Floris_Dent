from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from doctori.models import Doctor
from doctori.forms import DoctorForm


class DoctoriListView(ListView):
    template_name = 'doctori/list_of_doctori.html'
    model = Doctor
    context_object_name = 'all_doctors'


class DoctoriCreateView(CreateView):
    template_name = 'doctori/create_doctori.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('create-doctori')


class DoctoriUpdateView(UpdateView):
    template_name = 'doctori/update_doctori.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('list-of-doctori')
    # permission_required =


def delete_doctor(request, pk):
    Doctor.objects.filter(id=pk).delete()
    return redirect('list-of-doctori')