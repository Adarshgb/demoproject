from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from demoapp.forms import loginform, userdataform


def index(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_user:
                return redirect(managerview)

        else:
            messages.info(request, ' Invalid Credentials ')

    return render(request, 'index.html')


def register(request):
    login_form = loginform()
    userdata_form = userdataform()
    if request.method == "POST":
        login_form = loginform(request.POST)
        userdata_form = userdataform(request.POST, request.FILES)
        if login_form.is_valid() and userdata_form.is_valid():
            user = login_form.save(commit=False)
            print(user)
            user.is_user = True
            user.save()
            c= userdata_form.save(commit=False)
            c.user = user
            c.save()
            print(c)
            messages.info(request,'registration successfully')
        return redirect('index')
    return render(request, 'register.html', {'login_form': login_form ,'userdata_form':userdata_form})


def managerview(request):
    return render(request, 'manager.html')


def adminpage(request):
    return render(request, 'admin.html')
