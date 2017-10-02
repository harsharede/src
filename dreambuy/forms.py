from django import forms
from django.contrib.auth.models import User

from .models import  Product


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)