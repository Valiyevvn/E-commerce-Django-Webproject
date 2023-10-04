from django.contrib import admin
from .models import Settings, ContactFormMessage, UserProfile


# Register your models here.
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    list_filter = ['status',]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','adress','city','country','image_tag',]


admin.site.register(Settings,)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
