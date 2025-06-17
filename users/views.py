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
            # login(request, user) Automatically log the user in
            return redirect('login')  # Replace 'home' with your home page URL name
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})