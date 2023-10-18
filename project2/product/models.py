from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.forms import ModelForm

from django.utils.safestring import mark_safe
from mptt.models import MPTTModel,TreeForeignKey
from project2.custom_storages import DocumentStorage,ImageSettingStorage


class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False',"Hayir"),
    )
    title=models.CharField(max_length=30)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,storage=ImageSettingStorage())
    status=models.CharField(max_length=10,choices=STATUS) #admin paneli ucundur.

    slug=AutoSlugField(populate_from='title',unique=True)
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)

    create_at=models.DateField(auto_now_add=True)
    uptade_at=models.DateField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self):
        full_path= [self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False',"Hayir"),
    )

    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE) #kategori ile iliski
    title=models.CharField(max_length=70)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,storage=ImageSettingStorage())
    price=models.FloatField()
    amount=models.IntegerField()
    detail=RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS) #admin paneli ucundur.
    slug=AutoSlugField(populate_from='title',unique=True)
    create_at=models.DateField(auto_now_add=True)
    uptade_at=models.DateField(auto_now=True)



    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title




class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,storage=ImageSettingStorage())

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', "Evet"),
        ('False','Hayır'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    comment=models.TextField(max_length=100)
    rate=models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS,default='New')  # admin paneli ucundur.
    ip=models.CharField(blank=True,max_length=20)
    create_at = models.DateField(auto_now_add=True)
    uptade_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment','rate']



