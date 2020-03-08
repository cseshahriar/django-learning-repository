from django.urls import path
from pages.views import home, about, contact

urlpatterns = [  
    path('about/', about, name='about'),    
    path('contact/', contact, name='contact'),    
]