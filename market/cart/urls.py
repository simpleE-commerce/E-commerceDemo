from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartView.as_view(), name="cart_list"),
    path('addcart/', views.AddCartView.as_view(), name='add_to_cart'),
    path('update-quantity/', views.UpdateQuantityView.as_view(), name='update_quantity'),
    path('delete-item/', views.DeleteItemCart.as_view, name='delete_item'),
]
