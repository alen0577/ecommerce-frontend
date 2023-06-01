from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('fashion_page/men',views.fashionpage,name='fashionpage'),
    path('product_view/',views.product_view,name='product_view'),
    path('cart/',views.cart,name='cart'),
    
]
