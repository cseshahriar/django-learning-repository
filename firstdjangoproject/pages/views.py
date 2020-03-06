from django.shortcuts import render
from django.http import HttpResponseRedirect
from pages.models import Contact

# Create your views here.  
def home(request):
    return render(request, 'index.html', {'title': 'Home Page Title'})

def about(request):
    return render(request, 'about.html',  {'title': 'About Page Title'})
 
def contact(request):
    if(request.method == 'GET' and request.GET.get('method') == 'delete' and request.GET.get('id')):
        record = Contact.objects.filter(id=request.GET.get('id'))
        record.delete()
    
    if(request.method == 'GET' and request.GET.get('method') == 'edit' and request.GET.get('id')):
        record = Contact.objects.filter(id=request.GET.get('id')).get()
        return render(request, 'edit.html', {'title': 'Edit page title', 'data': record}) 

    if(request.method == 'POST'):
        if(request.GET.get('method') == 'update'):
            record = Contact.objects.filter(id=request.GET.get('id'))
            record.update(
                name = request.POST['name'], 
                email = request.POST['email'],
                address = request.POST['address'],
                city = request.POST['city'],
                zipcode = request.POST['zipcode']
            )
            return HttpResponseRedirect('/contact')
        else: 
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
