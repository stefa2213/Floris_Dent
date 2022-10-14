from django.urls import path, re_path
from pacienti import views
from pacienti.views import *
from django.conf import settings

urlpatterns = [
    path('create_pacienti/', views.PacientiCreateView.as_view(), name='create-pacienti'),
    path('list_of_pacienti/', views.PacientiListView.as_view(), name='list-of-pacienti'),
    path('update_pacienti/<int:pk>/', views.PacientiUpdateView.as_view(), name='update-pacienti'),
    path('detail_pacienti/<int:pk>/', views.PacientiDetailView.as_view(), name='detail-pacienti'),
    path('delete_pacient_modal/<int:pk>/', views.delete_pacient, name='delete-pacient-modal'),
]