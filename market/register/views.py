from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegisterForm
from core.models import *

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = User.objects.get(username=request.POST['username'])
            Person(user_info=new_user).save()
            new_customer = Person.objects.get(user_info=new_user)
            Customer(person_info=new_customer).save()
            return redirect(reverse('login'))
        else:
            return render(request, 'register/register_template.html', {'form': form})
    return render(request, 'register/register_template.html', {'form': form})
