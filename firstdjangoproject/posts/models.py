from django.db import models
from django import forms 
from django.core import validators  
from django.core.validators import ValidationError 


# Database Table 
class Posts(models.Model): 
    # model level validation
    def min_length_check(val):
        if len(val) < 3:
            raise ValidationError('Title must grater than 2', params={'val':val})

    title = models.CharField(validators=[min_length_check], max_length=255) 
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = models.Manager 
    # admin panel how to display 
    def __str__(self):
        return self.title


# category
class Category(models.Model): 
    # model level validation
    def min_length_check(val):
        if len(val) < 3:
            raise ValidationError('Title must grater than 2', params={'val':val})

    title = models.CharField(validators=[min_length_check], max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = models.Manager 
    # admin panel how to display 
    def __str__(self):
        return self.title


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



# Category form 
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
