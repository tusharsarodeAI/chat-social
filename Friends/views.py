from django.shortcuts import render,HttpResponse
from django.contrib.auth.admin import User
from Profile.models import User_Profile

# Create your views here.


def addfriend(request):
    othuser=User_Profile.objects.filter(username=request.user)
    if othuser:
        user =User_Profile.objects.all()
        return render(request,'Add Friend.html',{'user':user})

