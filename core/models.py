
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .helpers import *


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
    description =  models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255,unique_for_date='publish',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Posts')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
 
    def save(self,*args,**kwargs):
        self.slug =generate_slug(self.title)
        super(Post, self).save(*args,**kwargs)


class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
















































































class sendMaill(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

