from django.shortcuts import render , redirect
from .forms import UserAdminCreationForm
from django.contrib.auth import authenticate
from django.contrib import auth

def index(request):
    return render(request,'index.html')


def register(request):
    form = UserAdminCreationForm()
    
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        
        if form.is_valid():
            form.save();
            return redirect('login')
    
    return render(request,'register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')