from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('locatie/', views.LocationTemplateView.as_view(), name='locatie'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('galerie/', views.GalerieTemplateView.as_view(), name='galerie'),
    path('create_mesaj/', views.MesajCreateView.as_view(), name='create-mesaj'),
    path('detail_mesaj/<int:pk>/', views.MesajDetailView.as_view(), name='detail-mesaj'),
    path('list_of_mesaje/', views.MesajListView.as_view(), name='list-of-mesaje'),
    path('list_of_mesaje_arhivate/', views.MesajListViewArhivate.as_view(), name='list-of-mesaje-arhivate'),
    path('create_mesaj_succes/', views.MsgSuccessTemplateView.as_view(), name='create-mesaj-succes'),
    path('programare_succes/', views.ProgramareSuccessTemplateView.as_view(), name='programare-succes'),
    path('rezolvare_mesaj/<int:pk>/', views.rezolvare_mesaj, name='rezolvare-mesaj'),
    path('nerezolvare_mesaj/<int:pk>/', views.nerezolvare_mesaj, name='nerezolvare-mesaj'),
    path('sterge_mesaj/<int:pk>/', views.sterge_mesaj, name='sterge_mesaj'),
]
