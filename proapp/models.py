from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class log(AbstractUser):
    is_user=models.BooleanField(default=False)

class registerdata(models.Model):
    user=models.ForeignKey(log,on_delete=models.CASCADE,related_name='register')
    name= models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(10)
    image=models.ImageField(null=True,blank=True)

def __str__(self):
    return self.name