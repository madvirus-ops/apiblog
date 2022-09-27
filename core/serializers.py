from rest_framework import serializers
from .models import Post,Product
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PostSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content','owner','id','slug','image']

        # def create(self,validated_data):
        #     return Post.objects.create(validated_data,ignore_conflicts=False)
        

    # def post_exists(self,validated_data):
    #     title = validated_data['title']
    #     content = validated_data['content'] 
    #     if Post(title,content).exists():
    #         return True
    #     return False

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(email=validated_data['email'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user