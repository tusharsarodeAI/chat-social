from django.db import models 
from django.contrib.auth.models import User
from _datetime import date
# Create your models here.


class Post(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    image=models.ImageField(upload_to="Post")
    date=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)+" "+str(date.today())