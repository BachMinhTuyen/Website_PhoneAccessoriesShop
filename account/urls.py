from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]