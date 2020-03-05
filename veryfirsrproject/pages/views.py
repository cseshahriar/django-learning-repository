from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def member(request, id):
    return HttpResponse("<h1>Team Member ID: {}</h1>".format(id))

    
def team(request):
    return HttpResponse("<h1>Team Member List</h1>") 


 