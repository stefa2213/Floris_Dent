from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from doctori.forms import DoctorForm
from doctori.models import Doctor


class DoctoriListView(ListView):
    template_name = 'doctori/list_of_doctori.html'
    model = Doctor
    context_object_name = 'all_doctors'


class DoctoriCreateView(LoginRequiredMixin, CreateView):
    template_name = 'doctori/create_doctori.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('create-doctori')


class DoctoriUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'doctori/update_doctori.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('list-of-doctori')
    # permission_required =


@login_required
@permission_required('doctor.delete_doctor')
def delete_doctor(request, pk):
    Doctor.objects.filter(id=pk).delete()
    return redirect('list-of-doctori')