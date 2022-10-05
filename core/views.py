from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response 
from . models import Product,Post, Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import generics,status
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .serializers import PostSerial,UserSerial
from .forms import sendmaill
from django.core.mail import send_mail
from .forms import ProfileForm

from core import serializers


# import json

# # Create your views here.
# @api_view(["GET","POST"])
# def home(request):
#     data_list = Product.objects.all()#
#     data = {}
#     if data_list:
#         data['name'] = data_list.name
#         data['price'] = data_list.price
#         return Response(data)    
#     return Response(data)



class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerial




class ApiGenerics(generics.CreateAPIView):
    serializer_class = PostSerial
    queryset = Post.objects.all()
    authentication_classes = {TokenAuthentication,}
    permission_classes = {IsAuthenticated,}

    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)
        # semd_mail()
        return Response(self.data,status=status.HTTP_201_CREATED)

    def perform_create(self,serializer):
        serializer.save()
        self.data = {}
        self.data['message'] = "CREATED"
        self.data['id'] = serializer.data['id']
        self.data['title'] = serializer.data['title']
        self.data['slug'] = serializer.data['slug']
        self.data['content'] = serializer.data['content']
        self.data['image'] = serializer.data['image']
        return self.data


class ApiGenericsret(generics.RetrieveAPIView):
    serializer_class = PostSerial
    queryset = Post.objects.all()
    #this filed will come later
    # lookup_url_kwarg = 'pk'
    # authentication_classes = {TokenAuthentication,}
    # permission_classes = {IsAuthenticated,}
    #this too
    # ?lookup_field = 'pk'

class ApiGenericsupd(generics.RetrieveUpdateAPIView):
    serializer_class = PostSerial
    queryset = Post.objects.all()
    #this filed will come later
    # lookup_url_kwarg = 'pk'
    # authentication_classes = {TokenAuthentication,}
    # permission_classes = {IsAuthenticated,}
    #this too
    # ?lookup_field = 'pk'

class ApiGenericsdes(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerial
    queryset = Post.objects.all()

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message":"post deleted"},status=status.HTTP_200_OK)

    def perform_destroy(self,instance):
        instance.delete()

class PostDetail(APIView):
    authentication_classes = {TokenAuthentication,}
    permission_classes = {IsAuthenticated,}
    def get(self, request, pk):
        posts = get_object_or_404(Post, pk=pk)
        if posts:
            data = PostSerial(posts).data
            return Response(data)
        return Response(data.errors)   

class PostListCreate(APIView):
    authentication_classes = {TokenAuthentication,}
    permission_classes = {IsAuthenticated,}
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerial(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def post(self,request,*args, **kwargs):
        serializer = PostSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
           # status = 200
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)





#for creating without api
class ProfileCreateView(CreateView):
	model = Profile
	fields = ['bio','image']
    # forms_class = ProfileForm
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ProfileView(DetailView):
    model = User
    context_object_name = "user" 

    template_name = 'core/profile.html'







def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,publish__year=year,publish__day=day,publish__month=month)
    return render(request,'core/detail.html',{'post':post})

def postlist(request):
    posts = Post.objects.all()
    return render(request,'core/list.html',{'posts':posts})






































































































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
        
        