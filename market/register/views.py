from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return render(request, 'register/register_template.html', {'form': form})
    return render(request, 'register/register_template.html', {'form': form})
