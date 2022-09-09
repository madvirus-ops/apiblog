from rest_framework import serializers
from .models import Post,Product

class PostSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content']
    