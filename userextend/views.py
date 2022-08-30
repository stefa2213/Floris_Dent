from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from Floris_Dent.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            noul_cont = form.save()
            subject = 'Un nou cont'

            message = None
            my_html_msg = render_to_string('email/email_signup.html', {'new_user': noul_cont})
            send_mail(subject, message, EMAIL_HOST_USER, [noul_cont.email], html_message=my_html_msg)

            return redirect('login')
