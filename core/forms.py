
from dataclasses import fields
from django import forms
from .models import sendMaill,Comment,Profile
from core import models


class sendmaill(forms.ModelForm):
    class Meta:
        model = sendMaill
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        
class ProfileForm(forms.ModelForm):
    bio = forms.CharField()
    class Meta:
        model = Profile
        fields =('bio','image')