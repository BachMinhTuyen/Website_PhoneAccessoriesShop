from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
]