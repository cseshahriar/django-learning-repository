from django.urls import path
from pages.views import home, contact 

urlpatterns = [
    path('', home.as_view()),  
    path('contact/', contact.as_view()),  
] 
  