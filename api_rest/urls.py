from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.get_contact, name='get_all_contacts'),
    path('contacts/', views.contact_manager, name='contact_manager'),
]