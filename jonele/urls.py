from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('allproducts/', views.allproducts, name='allproducts'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('cart/', views.cart, name='cart') 
] 


