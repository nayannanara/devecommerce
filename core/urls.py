from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('conta/', include('accounts.urls', namespace="accounts")),
    path('checkout/', include('checkout.urls', namespace="checkout")),   
]
