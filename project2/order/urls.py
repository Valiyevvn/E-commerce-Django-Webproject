from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='order'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart'),
    path('orderproduct/',views.orderproduct,name='orderproduct')



]