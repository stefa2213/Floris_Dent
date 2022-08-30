from django.urls import path
from doctori import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list_of_doctori/', views.DoctoriListView.as_view(), name='list-of-doctori'),
    path('create_doctori/', views.DoctoriCreateView.as_view(), name='create-doctori'),
    path('update_doctori/<int:pk>/', views.DoctoriUpdateView.as_view(), name='update-doctori'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete-doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
