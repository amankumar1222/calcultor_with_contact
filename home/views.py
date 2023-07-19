from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , "index.html")

def math_fun(request):
    return render(request , "mathT.html")

def contact(request):
    return render(request , "contact.html")
