from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})