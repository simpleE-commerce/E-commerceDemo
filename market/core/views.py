from django.shortcuts import render
from django.views import generic


# Create your views here.


class MainClassView(generic.TemplateView):
    template_name = 'core/main.html'
