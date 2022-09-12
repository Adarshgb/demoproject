
from django.urls import path

from demoapp import views, userviews

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('managerview',views.managerview,name='managerview'),
    path('adminpage',views.adminpage,name='adminpage'),



    path('profileview',userviews.profileview,name='profileview'),




]