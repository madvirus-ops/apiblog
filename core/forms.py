from django import forms
from .models import sendMaill


class sendmaill(forms.ModelForm):
    class Meta:
        model = sendMaill
        fields = "__all__"