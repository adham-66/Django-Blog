from distutils.command.upload import upload
from operator import mod
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts/')
    
    
    
    def __str__(self):
        return self.title