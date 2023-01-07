from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to="Profile")
    friends=models.IntegerField(default=0)
    bio=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return str(self.username)

