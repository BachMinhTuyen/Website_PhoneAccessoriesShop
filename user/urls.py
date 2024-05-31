from django.urls import path
from . import views # call to url_shortener/views.py

urlpatterns = [
    path('', views.profile, name='profile'),
    path('updateProfile/', views.updateProfile, name="updateProfile"),
    path('updatePassword/',views.updatePassword, name='updatePassword'),
    path('receipt/', views.receipt, name='receipt'),
    path('receiptdetails/<int:MaHD>', views.receiptdetails, name='receiptdetails'),
    path('cancelOrder/<int:MaHD>', views.cancelOrder, name='cancelOrder'),
    path('receivedOrder/<int:MaHD>', views.receivedOrder, name='receivedOrder'),
]