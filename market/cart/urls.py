from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartView.as_view(), name="cart_list"),
    path('addcart/', views.AddCartView.as_view(), name='add_to_cart'),f
]
