from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductsListClassView.as_view(), name="product_show-page")
]
