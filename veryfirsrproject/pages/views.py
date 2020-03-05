from django.shortcuts import render
 
# Create your views here.
def home(request):
    return render(request, 'index.html', {'title' : 'Home Page Title'})

def about(request):
    return render(request, 'about.html',  {'title' : 'About Page Title'})

def contact(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        zipcode = request.POST['zip']
        return render(request, 'contact.html',  {'title' : 'Contact Page Title', 'email' : email, 'address' : address, 'city' : city, 'zipcode' : zipcode})
    return render(request, 'contact.html',  {'title' : 'Contact Page Title'})


 