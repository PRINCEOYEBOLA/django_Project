from django.shortcuts import render, redirect

# Create your views here.

def customers(request):
    return render(request, "customers/ourcare.html")

def register(request):
    return render(request, "customers/register.html")

def signin (request):
    return render(request, "customers/signin.html")