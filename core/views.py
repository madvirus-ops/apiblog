from django.shortcuts import render
from rest_framework.response import Response 
from . models import Product,Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics 
from .serializers import PostSerial
from .forms import sendmaill
from django.core.mail import send_mail


# import json

# Create your views here.
# @api_view(["GET","POST"])
# def home(request):
#     data_list = Product.objects.all()#
#     data = {}
#     if data_list:
#         data['name'] = data_list.name
#         data['price'] = data_list.price
#         return Response(data)
        
#     return Response(data)

class ApiGenerics(generics.GenericAPIView):
    query_set = Post.objects.all()
    

class ApiViewBlog(APIView):
    permission_classes = {IsAuthenticated,}
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerial(posts,many=True)
        return Response(serializer.data)
        

    def post(self,request,*args, **kwargs):
        serializer = PostSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

def sendinblue(request):
    if request.method == "POST":
        form = sendmaill(request.POST)
        
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            send_mail(subject,message,email,['contact@cybersafecal.com'],fail_silently=False,)
            return redirect('k')
    else:
        form = sendmaill()
    return render(request,'core/mail.html',{'form':form})    
        
        