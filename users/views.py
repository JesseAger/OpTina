from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# def user(request):
#     context={}
#     return render(request, 'users/signup.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# def login_view(request):

#     login(request, user) 
