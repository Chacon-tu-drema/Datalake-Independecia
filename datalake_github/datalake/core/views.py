from django.shortcuts import render


# Create your views here.

def home(request):

  return render(request,"core/home.html")

def quienes(request):

  return render(request,"core/quienes.html")

def qya(request):

  return render(request,"core/qya.html")