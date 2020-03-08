from django.db import models
from django import forms 
from django.core import validators 
from django.core.validators import ValidationError 


# Database Table 
class Posts(models.Model):
    def min_length_check(val):
        if len(val) <= 2:
            raise validators.ValidationError('Al least 2 character required')

    title = models.CharField(validators=[validators.validate_email],max_length=255) 
    content = models.TextField(validators=[min_length_check])  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = models.Manager 

# Html form 
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts  
        fields = ['title', 'content'] 
