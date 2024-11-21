from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomerSubmitblogForm(ModelForm):
    class Meta:
        model=submit_blog
        fields=['name','blog_type','email','blog_image','description']
        widgets = {
            'name': forms.TextInput(attrs={'disabled':True})
        }

class ContactForm(ModelForm):
    class Meta:
        model=contact_us
        fields='__all__'

class CustomerForm1(ModelForm):
    class Meta:
        model=User
        fields='__all__'