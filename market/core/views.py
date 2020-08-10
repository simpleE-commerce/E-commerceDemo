from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.


class MainClassView(generic.ListView):
    template_name = 'core/index.html'
    model = Product
    context_object_name = 'products'