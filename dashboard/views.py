from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context= {}
    return render(request, 'dashboard/home.html', context)