from django.urls import path
from programari import views

urlpatterns = [
    path('create_programare/', views.ProgramariCreateView.as_view(), name='create-programare'),
    path('list_of_programari/', views.ProgramareListView.as_view(), name='list-of-programari'),
    path('list_of_programari_anulate/', views.ProgramareListViewAnulate.as_view(), name='list-of-programari-anulate'),
    path('update_programare/<int:pk>/', views.ProgramariUpdateView.as_view(), name='update-programare'),
    path('detail_programare/<int:pk>/', views.ProgramariDetailView.as_view(), name='detail-programare'),
    path('inactive_programare/<int:pk>/', views.inactive_programare, name='inactive-programare'),
    path('active_programare/<int:pk>/', views.active_programare, name='active-programare'),
    path('delete_programare_modal<int:pk>/', views.delete_programare, name='delete-programare-modal'),
]
