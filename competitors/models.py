from django.db import models
from django.core.validators import *
from django.forms import NullBooleanField

# Create your models here.
# Create your models here.
class Competitor(models.Model):    
    name= models.CharField(max_length=100)
    description= models.TextField()
    Images= models.ImageField(blank=True)    #The image size must have width of 742px and height of 461px
    file = models.FileField(upload_to='files',blank=True)

class key(models.Model):
    Competename= models.CharField(max_length=100, null=True)
    Keyword = models.TextField(blank=True)
    Search= models.IntegerField(blank=True)
    Difficulty= models.IntegerField(blank=True)