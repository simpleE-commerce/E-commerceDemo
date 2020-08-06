from django.shortcuts import render
from django.views import generic
from core.models import Product


class ProductsListClassView(generic.ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
