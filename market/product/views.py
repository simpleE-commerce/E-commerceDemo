from django.shortcuts import render
from django.views import generic
from core.models import Product
from django.http import HttpResponse


class ProductsListClassView(generic.ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class SearchView(generic.TemplateView):
    template_name = 'product/index.html'
    model = Product
    
    def get(self, request, *args, **kwargs):
        print(request.GET['term'])
        products = Product.objects.filter(product_name__icontains=request.GET['term'])
        products
        return render(request, self.template_name, {"products": products})