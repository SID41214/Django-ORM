from django.urls import path
from app import views

urlpatterns = [
   path('',views.home,name='home'),
   path('order',views.order_product,name='order-product'),
    
]