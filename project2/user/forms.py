from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput,FileInput,Select
from home.models import UserProfile
from django import forms

class UserUptadeForm(UserChangeForm):
    class Meta:
        model=User
        fields = ('username','email','first_name','last_name')
        widgets = {
            'username' : TextInput(attrs={'class' : 'form-control','placeholder' : 'username'}),
            'email' : EmailInput(attrs={'class' : 'form-control','placeholder' : 'email'}),
            'first_name' : TextInput(attrs={'class' : 'form-control','placeholder' : 'firstname'}),
            'last_name' : TextInput(attrs={'class' : 'form-control','placeholder' : 'lastname'}),


        }

CITY = [
    ('Baki','Baki'),
    ('Sumqayit','Sumqayit'),
    ('Novxani','Novxani'),
]

class ProfileUptadeForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone','adress','city','country','image')
        widgets= {
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'adress'}),
            'city': Select(attrs={'class': 'form-control', 'placeholder': 'city'},choices=CITY),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'image': FileInput(attrs={'placeholder': 'image'}),
        }