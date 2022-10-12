from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    body = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    customer  = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.body[0:10]
