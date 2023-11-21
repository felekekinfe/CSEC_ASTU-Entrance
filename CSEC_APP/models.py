from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class Members(AbstractUser):
    department=models.CharField(max_length=100)
    ID_Number=models.CharField(max_length=20)
    Roll=models.CharField(max_length=200)

    class Meta: 
        verbose_name_plural='Members'

class Events(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    date=models.DateTimeField()
    time=models.TimeField()
    venue=models.CharField(max_length=200)
    organizer=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='Events'
        
    def __str__(self):
        return self.title
    
    

    