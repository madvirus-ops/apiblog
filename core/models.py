from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#coding for entrepreneurs api
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def sale_price(self):
        return "%.2f" %float((self.price)* 0.8)
    
#just django api
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class sendMaill(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

