from django import forms
from .models import Feddback
from django.db import models
from django.forms import ModelForm

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feddback

        fields =['name','email','phone','text']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'your name'}),
            'email': forms.TextInput(attrs={'placeholder': 'your e-mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'your phone'}),
            'text': forms.Textarea(attrs={'placeholder': 'your message'})
        }