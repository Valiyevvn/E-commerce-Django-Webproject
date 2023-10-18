from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import ModelForm, TextInput,Textarea
from django.core.validators import validate_email
from django.utils.safestring import mark_safe
from project2.custom_storages import DocumentStorage,ImageSettingStorage

# Create your models here.
class Settings(models.Model):

    STATUS = (
                ('True', 'Evet'),
        ('False', "Hayir"),
    )
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    adress = models.CharField(max_length=150,blank=True)
    phone = models.CharField(max_length=30,blank=True)
    fax = models.CharField(max_length=30,blank=True)
    email = models.CharField(max_length=50,blank=True)
    smtpserver = models.CharField(max_length=50,blank=True)
    smtpemail = models.CharField(max_length=150,blank=True)
    smtppassword = models.CharField(max_length=150,blank=True)
    smtpport = models.CharField(max_length=150,blank=True)
    icon = models.ImageField(blank=True,storage=ImageSettingStorage())
    logo = models.ImageField(blank=True,storage=ImageSettingStorage())
    facebook = models.CharField(blank=True,max_length=130)
    twitter = models.CharField(blank=True,max_length=130)
    instagram = models.CharField(blank=True,max_length=130)
    linkedin = models.CharField(blank=True,max_length=130)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)

    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateField(auto_now_add=True)
    uptade_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', "Read"),
    )
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=255)
    ip=models.CharField(blank=True,max_length=50)
    note=models.CharField(blank=True,max_length=50)
    status = models.CharField(max_length=20, choices=STATUS,default='New')
    create_at = models.DateField(auto_now_add=True)
    uptade_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields=['name','email','subject','message']



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)
    adress=models.CharField(max_length=150)
    city=models.CharField(max_length=20 )
    country=models.CharField(max_length=20 )
    image = models.ImageField(blank=True, storage=ImageSettingStorage())

    def __str__(self):
      return  self.user.username

    def user_name(self):
        return   self.user.first_name + ' ' +self.user.last_name + ' ' + '(' + self.user.username + ')'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','adress','city','country','image']


