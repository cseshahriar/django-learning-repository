from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to the home page</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')
