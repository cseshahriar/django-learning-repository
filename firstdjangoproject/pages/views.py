from django.shortcuts import render
from pages.models import Contact

# Create your views here. 
def home(request):
    return render(request, 'index.html', {'title': 'Home Page Title'})

def about(request):
    return render(request, 'about.html',  {'title': 'About Page Title'})
 
def contact(request):
    if(request.method == 'POST'):
        data = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            address = request.POST['address'],
            city = request.POST['city'],
            zipcode = request.POST['zipcode']
        )
        data.save()
    rows = Contact.objects.all() 
    return render(request, 'contact.html',  {'title': 'Contact Page Title', 'rows': rows})
