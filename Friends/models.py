from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Friends(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    total_friends = models.IntegerField()
    friends_name = models.CharField(max_length=1000)

    def __str__(self):
        return str(str(self.username))