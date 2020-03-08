from django.db import models
from django import forms 
from django.core import validators 
from django.core.validators import ValidationError 


# Database Table 
class Posts(models.Model): 
    title = models.CharField(max_length=255) 
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = models.Manager 

# Html form 
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts  
        fields = ['title', 'content']
    
    # non field validator 
    def clean(self):
        fields = self.cleaned_data
        keys = list(fields.keys()) 
        if(len(fields['title']) <= 3):
            raise validators.ValidationError("Title must be greater than 3", params={'val':keys[0]})
        if(len(fields['content']) <= 3):
            #%(val)s
            raise validators.ValidationError("Content must be greater than 3", params={'val':keys[1]})