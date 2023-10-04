from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class SearchForm(forms.Form):
    query=forms.CharField(label='Search',max_length=100)

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30,label='Istifadəçi adı', help_text='dad', widget=forms.TextInput(attrs={'placeholder': 'Istifadəçi adı'}))
    first_name = forms.CharField(max_length=30, label='Ad', widget=forms.TextInput(attrs={'placeholder': 'Ad'}))
    last_name = forms.CharField(max_length=30, label='Soyad', widget=forms.TextInput(attrs={'placeholder': 'Soyad'}))
    email = forms.EmailField(max_length=254, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))

    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




