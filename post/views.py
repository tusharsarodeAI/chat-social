from django.shortcuts import render,HttpResponse
from Profile.models import User_Profile,User
from post.models import Post
from Friends.models import Friends
# Create your views here.
def postpage(request):
    othuser=User.objects.filter(username=request.user)
    if othuser:
        '''othuser=othuser[0]
        post_obj=User_Profile.objects.get(username=othuser)
        friends=post_obj.friends_name
        if friends:
            print(friends)
            
            data={
                ''
            }'''
        post_obj=Post.objects.all()
        return render(request,'Post.html',{'post':post_obj})
    else:
        HttpResponse("Error 404")
