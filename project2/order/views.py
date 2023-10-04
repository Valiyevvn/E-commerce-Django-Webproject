from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import ShopCartForm, ShopCart, OrderForm,Order,OrderProduct
from django.contrib import messages
from django.utils.crypto import get_random_string
from product.models import Category
from home.models import Settings
from product.models import Product
import logging

from home.models import UserProfile



# Create your views here.
def index(request):
    return HttpResponse('adf')

@login_required(login_url='/login')
def addtocart(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct=ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control=1
    else:
        control=0

    if request.method == 'POST':
        form=ShopCartForm(request.POST)

        if form.is_valid():
            if control == 1:
                data=ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()



            else:
                data=ShopCart()
                data.user_id=current_user.id
                data.product_id=id
                data.quantity=form.cleaned_data['quantity']
                data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request,'Seçdiyiniz məhsul uğurla səbətə əlavə olundu. Təşəkkürlər ')
            return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()

        else:
           data = ShopCart()
           data.user_id = current_user.id
           data.product_id = id
           data.quantity = 1
           data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, 'Seçdiyiniz məhsul uğurla səbətə əlavə olundu. Təşəkkürlər ')
        return HttpResponseRedirect(url)


    messages.error(request,'Seçdiyiniz məhsul səbətə əlavə olunmadı. Yenidən yoxlayın ')
    return HttpResponseRedirect(url)



@login_required(login_url='/login')
def shopcard(request):
    setting=Settings.objects.get()
    category=Category.objects.all()
    current_user=request.user
    shopcard=ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    total=0
    for rs in shopcard:
        total += rs.product.price * rs.quantity

    return render(request,'pages/shopcard.html',context={
        'setting':setting,
        'shopcard':shopcard,
        'category':category,
        'total':total
    })

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    current_user=request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Məhsul səbətdən çıxarıldi.")
    return HttpResponseRedirect('/shopcart')

@login_required(login_url='/login')
def orderproduct(request):
    category=Category.objects.all()
    setting=Settings.objects.get()
    current_user = request.user
    shopcard = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcard:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name=form.cleaned_data['first_name']
            data.last_name=form.cleaned_data['last_name']
            data.address=form.cleaned_data['address']
            data.city=form.cleaned_data['city']
            data.phone=form.cleaned_data['phone']
            data.user_id=current_user.id
            data.total=total
            data.ip=request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper()
            data.code=ordercode
            data.save()

            shopcard=ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcard:
                detail=OrderProduct()
                detail.order_id =data.id
                detail.product_id=rs.product_id
                detail.user_id=current_user.id
                detail.quantity=rs.quantity
                detail.price=rs.product.price
                detail.amount=rs.amount
                detail.save()

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart-items']=0
            profile = UserProfile.objects.get(user_id=current_user.id)
            messages.success(request,'Sifarisiniz tamamlandi')
            return HttpResponseRedirect('/user/orders/')
        else:
            messages.error(request,form.errors)
            return  HttpResponseRedirect('/order/orderproduct')

    form=OrderForm()
    profile=UserProfile.objects.get(user_id=current_user.id)
    return render(request,'pages/order_form.html',context={
        'shopcard':shopcard,
        'total':total,
        'form':form,
        'profile' :profile,
        'category':category,
        'setting':setting
    })
