from django.urls import path
from preturi import views

urlpatterns = [
    path('create_preturi/', views.PreturiCreateView.as_view(), name='create-preturi'),
    path('list_preturi/', views.PreturiListView.as_view(), name='list-preturi'),
    path('list_preturi_dezactivate/', views.PreturiListViewAnulate.as_view(), name='list-preturi-dezactivate'),
    path('update_preturi/<int:pk>/', views.PreturiUpdateView.as_view(), name='update-preturi'),
    path('delete_pret_modal/<int:pk>/', views.delete_serviciu, name='delete-pret-modal'),
    path('deactivate_pret/<int:pk>/', views.deactivate_pret, name='deactivate-pret'),
    path('activate_pret/<int:pk>/', views.activate_pret, name='activate-pret'),
]
