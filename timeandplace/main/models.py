from django.db import models

# Create your models here.
class place(models.Model):
    placename = models.CharField(max_length=100)
    address = models.CharField(max_length=100) 
    placetype  = model.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=6)
