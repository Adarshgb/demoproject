from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class log(AbstractUser):
    is_user=models.BooleanField(default=False)

class userdata(models.Model):
    user=models.ForeignKey(log,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)


    def __str__(self):
        return self.name