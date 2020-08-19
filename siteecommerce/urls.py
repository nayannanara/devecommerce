from django.contrib import admin
from django.conf import settings
from django.urls import path, include
#from core import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
