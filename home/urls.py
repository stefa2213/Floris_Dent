from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('locatie/', views.LocationTemplateView.as_view(), name='locatie'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
]
