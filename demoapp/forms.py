from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import log, userdata


class loginform(UserCreationForm):

    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2=forms.CharField(widget=forms.PasswordInput,label='confirmpassword')
    class Meta:
        model = log
        fields = ('username','password1','password2')

class userdataform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ('name','address')