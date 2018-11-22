from django import forms
from django.contrib.auth.models import User
from beerapp.models import *
class BeerBarForm(forms.ModelForm):
        class Meta:
            model = BeerBar
            fields ='__all__'

class UserForm(forms.ModelForm):


    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
                               required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                            required=True, max_length=50)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First name'}), required=True,
        max_length=50)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last name'}), required=True,
        max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=50)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=50)


    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']