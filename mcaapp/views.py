from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *

def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def post(request):
    data=Post.objects.all()
    return render(request,'posts.html',{"data":data})

@login_required(login_url='/login/')
def createpost(request):
    if request.method=='POST':
        post=Post()
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('/posts')
    return render(request,'createpost.html')

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            user=User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password1)
            user.save()
            print("success")
            return redirect('/login')
        else:
            messages.info(request,'Password Not Match')
            return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
