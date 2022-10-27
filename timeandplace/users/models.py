# from django.db import models

class user(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.username

class authenticate(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=40)
    password = models.CharField(min_length=8)

class bio(models.Model):
    username = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=200)
    occupation = models.BooleanField()

