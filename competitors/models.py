from django.db import models
from django.core.validators import *

# Create your models here.
# Create your models here.
class Competitor(models.Model):    #Subject i.e. Digital forensics
    name= models.CharField(max_length=100)
    description= models.TextField()
    backlink= models.CharField(max_length=100)  #Available year
    DA= models.CharField(max_length=100)
    SERP= models.CharField(max_length=100)
    Images= models.ImageField(blank=True)    #The image size must have width of 742px and height of 461px
    file = models.FileField(upload_to='files',blank=True)