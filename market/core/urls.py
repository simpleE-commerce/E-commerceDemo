from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', MainClassView.as_view(), name='index')
]