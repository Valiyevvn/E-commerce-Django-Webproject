from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserUptadeForm,ProfileUptadeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from product.models import Category
from home.models import Settings
from order.models import Order
from home.models import UserProfile
from django.contrib import messages
from product.models import Comment
from order.models import OrderProduct


# Create your views here.
def index(request):
    category = Category.objects.all()
    setting = Settings.objects.get()

    current_user = request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    return render(request,'pages/user_profile.html',context={
        'category':category,
        'setting' : setting,
        'profile':profile,
    })


def user_uptade(request):
    if request.method =='POST':
        user_form=UserUptadeForm(request.POST,instance=request.user)
        profile_form=ProfileUptadeForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Hesabiniz yeniləndi !..")
            return redirect('/user')

        else:
            messages.warning(request,"Hesabınız yenilənmədi! Yenidən Yoxlayın ..")
            return redirect('/user/uptade')


    else:
        category = Category.objects.all()
        setting = Settings.objects.get()

        user_form=UserUptadeForm(instance=request.user)
        profile_form = ProfileUptadeForm(instance=request.user.userprofile)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)

        return render(request,'pages/user_uptade.html',context={
              'category': category,
              'setting': setting,
              'profile_form':profile_form,
              'user_form':user_form,
              'profile':profile

        })


def change_password(request):
    if request.method =='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Şifəniz yeniləndi! ..")
            return redirect('/user')
        else:
            messages.warning(request, "Şifrəniz yenilənmədi! Zəhmət olmasa formun qaydalarına riaət edin ..")
            return redirect('/user/password')


    else:
         category = Category.objects.all()
         setting = Settings.objects.get()
         form=PasswordChangeForm(request.user)
         current_user = request.user
         profile = UserProfile.objects.get(user_id=current_user.id)
         return render(request,'pages/change_password.html',context={
            'category': category,
            'setting': setting,
             'form':form,
             'profile':profile

         })
@login_required(login_url='/login')
def orders(request):
    current_user = request.user
    category = Category.objects.all()
    setting = Settings.objects.get()
    orders=Order.objects.filter(user_id=current_user.id)
    profile = UserProfile.objects.get(user_id=current_user.id)
    return render(request,'pages/user_orders.html',context={
        'category': category,
        'setting': setting,
        'profile': profile,
        'orders': orders

    })

@login_required(login_url='/login')
def order_detail(request,id):
    current_user = request.user
    category = Category.objects.all()
    setting = Settings.objects.get()
    order = Order.objects.get(user_id=current_user.id,id=id)
    orderitems=OrderProduct.objects.filter(order_id=id)
    profile = UserProfile.objects.get(user_id=current_user.id)
    return render(request, 'pages/user_order_detail.html', context={
        'category': category,
        'setting': setting,
        'profile': profile,
        'order': order,
        'orderitems':orderitems,

    })

@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    setting = Settings.objects.get()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    comments = Comment.objects.filter(user_id=current_user.id)
    return render(request,'pages/user_comments.html',context={
        'category': category,
        'setting': setting,
        'comments': comments,
        'profile': profile,
    })

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request, "Mesajınız başarıyla silindi ..")
    return HttpResponseRedirect('/user/comments')
