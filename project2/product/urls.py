from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name='index'),
    path('addcomment/<int:id>',views.addcomment,name='addcomment'),
]