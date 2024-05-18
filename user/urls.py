from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('', views.profile, name='profile'),
    path('receipt/', views.receipt, name='receipt'),
    path('receiptdetails/', views.receiptdetails, name='receiptdetails'),
]