from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.anasayfa,name='anasayfa'),
    path('iletisim/',views.iletisim,name='iletisim'),
    path('hakkimizda/',views.hakkimizda,name='hakkimizda'),
    path('referanslar/',views.referanslar,name='referanslar'),
    path('category/<int:id>/<slug:slug>/',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
]