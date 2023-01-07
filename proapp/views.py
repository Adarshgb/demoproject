from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from pro.forms import loginform, registerdataform


# Create your views here.



def register(request):
    login_form=loginform()
    registerdata_form=registerdataform()
    if request.method =="POST":
        home_page=home(request.POST)
        registerdata_form=registerdataform(request.POST,request.FILES)
        if home_page.is_valid() and registerdata_form.is_valid():
            user=home_page.save(commit=False)
            print(user)
            user.is_user=True
            user.save()
            register=registerdata_form.save(commit=False)
            register.user=user
            register.save()
            print(register)
        return redirect('home')
    return render(request,'register.html',{'login_form':login_form,'registerdata_form':registerdata_form})

def profile(request):
    return render(request,'profile.html')


def home(request):
    login_form=loginform()
    if request.method=='POST':
        login_form=loginform(request.POST,request.FILES)
        if login_form.is_valid():
            user=login_form.save(commit=False)
            user.is_user=True
            user.save()
            return redirect(home)
    return render(request,'home.html',{'login_form':login_form})