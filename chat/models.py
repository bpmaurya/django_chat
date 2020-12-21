from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
        
class User(models.Model):
    username = models.CharField( max_length=50)    
    first_name = models.CharField( max_length=50)    
    last_name = models.CharField( max_length=50)    
    email= models.CharField( max_length=50)    
    password = models.CharField( max_length=50)    