from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    return render(request, 'page/home.html')

def aboutus(request):
    return render(request, 'page/aboutUs.html')

def contact(request):
    return render(request, 'page/contact.html')