from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('produto/', views.product, name='product'),
    path('produtos/', views.product_list, name='product_list'),

]
