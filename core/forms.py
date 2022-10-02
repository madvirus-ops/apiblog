
from dataclasses import fields
from django import forms
from .models import sendMaill,Comment,Profile


class sendmaill(forms.ModelForm):
    class Meta:
        model = sendMaill
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"