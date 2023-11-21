
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .models import Members,Events
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MembersRegistrationForm(UserCreationForm):
    
    class Meta:
        model=Members
        fields=['username','ID_Number','Roll','department','email','password1','password2']
    

class AddEventForm(forms.ModelForm):

    class Meta:
        model=Events
        fields=['title','description','date','time','venue','organizer']

