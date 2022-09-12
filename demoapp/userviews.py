from django.shortcuts import render

from demoapp.models import userdata


def profileview(request):
    u=request.user
    data=userdata.objects.filter(user=u)
    return render(request,'usertemp/profileview.html',{'data':data})