from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='anasayfa'),
    path('uptade/',views.user_uptade,name='user_uptade'),
    path('password/',views.change_password,name='change_password'),
    path('orders/',views.orders,name='orders'),
    path('orderdetail/<int:id>',views.order_detail,name='orderdetail'),
    path('comments/',views.comments,name='comments'),
    path('deletecomment/<int:id>',views.deletecomment,name='deletecomment'),



]
