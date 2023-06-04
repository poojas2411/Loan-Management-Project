from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from web.views import home
from django.contrib.auth import logout
# Create your views here.
def acc(request):
    if(request.method=="GET"):
        return render(request,'login.html')
    elif(request.method=="POST"):
        user=request.POST['username']
        passw=request.POST['password']
        print(user)
        print(passw)
        user=authenticate(username=user,password=passw)
        print("i am password",user)
        if user is not None:
            print(user)
            login(request,user)
            return home(request)
        else:
            return render(request,'login.html',{'message':"password or username is wrong plz try again"}) 

def regis(request):
    if(request.method=="GET"):
        return render(request,'regi.html')
    elif(request.method=="POST"):
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        compassword=request.POST['confirm-password']
        if(password==compassword):
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return render(request,'login.html',{'message':'Account Created  sucessfuly now you can login'})
        else:
            return render(request,'regi.html',{'message':'password doest not match try again'})

        
def out(request):
    logout(request)
    return redirect('acc')