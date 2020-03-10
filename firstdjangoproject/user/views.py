from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib import messages 

# Create your views here.
def login(request): 
    # create login form 
    form = AuthenticationForm()
    return render(request, 'login.html', {'title': 'User Login', 'form': form})

def register(request):
    # create form template 
    form = UserCreationForm()
    # form submit data store
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User successfully registered')
            return redirect('/user/login') 

    # view get request form template 
    return render(request, 'register.html', {'title':'User Register', 'form': form})   