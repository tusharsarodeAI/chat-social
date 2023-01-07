from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout
from Profile.models import User_Profile
from Social_Website.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random

otp=0
def home(request):
    return render(request,'login.html')

def logIn(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        password = request.POST.get('Password')
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/main')
        else:
            messages.error(request,'User Not Exist ...!!!')
            return redirect('/')
    else:
        return render(request,'Login.html',)

def createacc(request):
    return render(request,'SignUp.html')

def signup(request):

    if request.method=='POST':
        username=request.POST.get('Username')
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        password1 = request.POST.get('Password')
        password2 =request.POST.get('RPassword')
        email =request.POST.get('Email')
        if len(password1)>2:
            if password1==password2:
                if User.objects.filter(username=username):
                    messages.Error(request,'Username Already Taken ...!!!')
                    return redirect('/createacc')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    password=password1, email=email)
                    user.save()
                    return render(request, 'login.html')
            else:
                messages.error(request,'Passwoed Does Not Matched...!!!')
                return redirect('/createacc')
        else:
            messages.error(request,'Password should contain Number ,Alphabets And Length of password should greater than 8 character')
            return redirect('/createacc')
    else:
        messages.error(request,'404 - Error Found ')
        return redirect('/createacc')

def forgetpass(request):
    return render(request,'varification.html')

def varification1(request):
    if request.method=="POST":
        user_id=request.POST.get('text')
        databaseid=User.objects.filter(username=user_id)
        print(databaseid)
        if databaseid:
            uid=databaseid[0].email
            print(uid)
            global otp
            otp = random.randint(111111, 999999)
            subject=' One Time Password'
            message=str(otp)
            recepient=str(uid)
            send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
            return redirect('/forgetpass')
        else:
            messages.error(request,' No sush Email Address Exist In Database')
            return redirect("/")

def varification2(request):
    if request.method=="POST":
        getotp=request.POST.get('OTP')
        print(getotp)
        print(type(getotp))
        global otp
        print(otp)
        otp=str(otp)
        if otp==getotp:
            return HttpResponse(" Enter new Password....")
        else:
            messages.error(request,'<h1> No sush Email Address Exist In Database</h1>')
            return redirect('/varification')

def logOut(request):
    logout(request)
    messages.success(request, "User Log Out Successfully ...")
    return redirect("/")

