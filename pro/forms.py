from django.contrib.auth.forms import UserCreationForm
from django import forms

from proapp.models import log, registerdata


class loginform(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput,label='password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='confimpassword')
    class Meta:
        model=log
        fields=('username','password1','password2')
class registerdataform(forms.ModelForm):
    class Meta:
        model=registerdata
        fields=('name','email','number','image')