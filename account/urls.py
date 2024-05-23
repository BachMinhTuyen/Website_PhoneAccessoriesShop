from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]