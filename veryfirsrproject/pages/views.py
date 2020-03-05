from django.shortcuts import render
 
# Create your views here.
def home(request):
    return render(request, 'index.html', {'title' : 'Home Page Title'})

def about(request):
    return render(request, 'about.html',  {'title' : 'About Page Title'})

def contact(request):
    return render(request, 'contact.html',  {'title' : 'Contact Page Title'})


 