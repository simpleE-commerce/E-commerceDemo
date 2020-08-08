from django.shortcuts import render
from django.views import generic
from core.models import Product


class ProductsListClassView(generic.ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class ProductDetailClassView(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    # def get_queryset(self):
    #     return Product.objects.filter(id=)