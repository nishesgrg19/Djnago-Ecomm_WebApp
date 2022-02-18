from re import template
from unicodedata import name
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import PasswordReset,Passwordconfirm
urlpatterns = [
    path('', views.Productview.as_view(),name='home'),
    path('product-detail/<int:id>', views.Product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('remove-cart/<int:id>',views.remove_cart,name='remove-cart'),
    path('cart/<int:id>',views.cart,name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('fashion/<slug:data>',views.fashion,name='fashion'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/',views.laptop,name='laptop'),
    path('laptop/<slug:data>',views.laptop,name='laptop'),
    path('loginn/',views.loggin,name='login'), 
    path('logout/',views.sign_out,name='sign-out'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('forget/',views.forget,name='forget'),
   
    
    

    
 
  
]

