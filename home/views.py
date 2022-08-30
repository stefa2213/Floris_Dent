from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from Floris_Dent.settings import EMAIL_HOST_USER


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


class LocationTemplateView(TemplateView):
    template_name = 'home/locatie.html'


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'


# def send_mail_reset(request):
#     form = EmailForm(request.POST)
#     if form.is_valid():
#         subject = 'Un nou cont'
#         my_html_msg = render_to_string('email/email_signup.html', {'new_user': noul_cont})
#         email_add = form.cleaned_data['email']
#         try:
#             send_mail(subject, message, EMAIL_HOST_USER, [email_add], html_message=my_html_msg)
#         except:
#             print("An exception occurred")
#
#         return redirect('login')