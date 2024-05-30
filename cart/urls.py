from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    # path('cart/', views.view_cart, name='view_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.process_order, name='process_order'),
]