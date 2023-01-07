from django.urls import path

from proapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile')
]