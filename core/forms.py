
from django import forms
from .models import sendMaill,Comment


class sendmaill(forms.ModelForm):
    class Meta:
        model = sendMaill
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        