from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),
    path('contacts/', views.contact_manager, name='contact_manager'),
    path('contacts/bulk-create/', views.bulk_create_contacts, name='bulk_create_contacts'),
]