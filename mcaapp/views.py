from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

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
            return redirect('/')
        else:
            messages.info(request,'Password Not Match')
            return redirect('/')
    else:
        return render(request,'register.html')