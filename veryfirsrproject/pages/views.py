from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

# Create your views here.
class home(View):
    def get(self, request):
        return HttpResponse('<h1>Welcome to the home page</h1>')

class contact(View):
    def get(self, request):
        return HttpResponse('<h1>Contact Us</h1>') 
 