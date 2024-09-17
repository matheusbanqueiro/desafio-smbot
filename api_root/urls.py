from django.contrib import admin
from django.urls import include, path
from .views import home 

urlpatterns = [
    path('', home, name='home'),
    # path('admin/', admin.site.urls),
    path('api/', include('contacts.urls'), name='contacts_urls'),
]
