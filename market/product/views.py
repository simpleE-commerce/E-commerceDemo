from django.shortcuts import render
from django.views import generic
from core.models import Product
from django.http import HttpResponse
from core.models import Product


class ProductsListClassView(generic.ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'

    def post(self, request, *args, **kwargs):
        print(request)

class SearchView(generic.TemplateView):

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.POST['term'])
        return HttpResponse("<h1>Post</h1>")
    
    def get(self, request, *args, **kwargs):
        print(request.GET['term'])
        queryset = Product.objects.filter(product_name__icontains=request.GET['term']).values("product_name")
        t = "<h1>"+queryset[0]['product_name']+"</h1>"
        return HttpResponse(t)