from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .decoraters import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def home(request):
    
    return render(request,'home.html')

def signup(request):
    form=createuserform()
    if request.method=='POST':
       
        form=createuserform(request.POST)
        if form.is_valid():
            uname=request.POST.get('username')
            email=request.POST.get('email')
            form.save()
            messages.success(request,"account created successfully")
            message = f'Hi {uname}, thank you for registering in TerraBlog Community'
            send_mail("Registration Successfull",message,"2100030498@kluniversity.in",[email], fail_silently=False,)
            return redirect('login')
        
    context={'form':form}
    return render(request,'signup.html',context)

@unautheticated_user
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"username or password is invalid")
    context={}
    return render(request,'login.html',context)

def management(request):
    Customer=User.objects.all()
    blogs=submit_blog.objects.all()
    contact=contact_us.objects.all()
    context={'Customer':Customer,'blogs':blogs,'contact':contact}
    return render(request,'management.html',context)

def logout_page(request):
    logout(request)
    return redirect('home')

def submit(request):
    initial_dict = {
        'name':request.user.username
    }
    form=CustomerSubmitblogForm(initial=initial_dict)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['name'] = request.user.get_username()
        form =CustomerSubmitblogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Property is Submitted Sucessfully')
        else:
            messages.MessageFailure(request,'enter the valid details')
    context={'form':form}
    return render(request,'create_blog.html',context)

def blogs_page(request):
    blogs=submit_blog.objects.all()
    context={'blogs':blogs}
    return render(request,'blogs.html',context)

def delete_order(request,pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        user.delete()
        return redirect('management')
    context={'item':user}
    return render(request,'delete_user.html',context)

def delete_blog(request,pk):
    blog=submit_blog.objects.get(id=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('management')
    context={'item':blog}
    return render(request,'delete_user.html',context)

def contact(request):
    con=ContactForm()
    if request.method == 'POST':
        con=ContactForm(request.POST)
        if con.is_valid():
            con.save()
            messages.success(request,'Your form is Submitted Sucessfully')
    context={'con':con}
    return render(request,'contact_us.html',context)

@login_required(login_url='login')
def datascience(request):
    data=submit_blog.objects.all()
    context={'data':data}
    return render(request,'datascience.html',context)

@login_required(login_url='login')
def cybersecurity(request):
    cyber=submit_blog.objects.all()
    context={'cyber':cyber}
    return render(request,'cybersecurity.html',context)

@login_required(login_url='login')
def devops(request):
    devops=submit_blog.objects.all()
    context={'devops':devops}
    return render(request,'devops.html',context)

@login_required(login_url='login')
def webtechnology(request):
    web=submit_blog.objects.all()
    context={'web':web}
    return render(request,'webtechnology.html',context)

@login_required(login_url='login')
def coding(request):
    coding=submit_blog.objects.all()
    context={'coding':coding}
    return render(request,'coding.html',context)

@login_required(login_url='login')
def cloudcomputing(request):
    cloud=submit_blog.objects.all()
    context={'cloud':cloud}
    return render(request,'cloudcomputing.html',context)

@login_required(login_url='login')
def customer(request, pk):
    customer=User.objects.get(id=pk)
    context={'customer':customer}
    return render(request,'viewuser.html',context)

def profile(request,pk):
    customer = User.objects.get(id=pk)
    context={'customer':customer}
    return render(request,'viewuser.html',context)

# def view(request,pk):
#     viewblog=submit_blog.object.get(id=pk)
#     context={'viewblog':viewblog}
#     return render(request,'blogs.html',context)