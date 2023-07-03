from django import forms
from django.contrib.auth.models import user
class signForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','password','email','first_name','lastname']
