from django.urls import path
from pages.views import member, team

urlpatterns = [
    path('members/', team, name='team'),
    path('member/<int:id>', member, name='member')    
]   
  