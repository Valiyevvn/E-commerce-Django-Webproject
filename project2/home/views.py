from django.contrib.auth import logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Settings, ContactFormMessage, ContactFormu, UserProfile
from django.contrib.auth import authenticate
from django.contrib import messages

from product.models import Product, Category,Images,Comment
from .forms import SearchForm, SignUpForm
import json

from order.models import ShopCart


# Create your views here.
def anasayfa(request):

    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    dealofday = Product.objects.all()[:4]
    lastproduct = Product.objects.all().order_by('-id')[:6]
    trendproduct = Product.objects.all().order_by('?')[:6]
    toprated = Product.objects.all().order_by('?')[:6]
    bestseller = Product.objects.all().order_by('?')[:4]
    productgrid = Product.objects.all().order_by('?')[:12]
    katagoriyarandom=Category.objects.all().order_by('?')[:8]
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()


    return render(request, 'pages/anasayfa.html',context = {'setting': setting, 'dealofday': dealofday, 'category': category, 'lastproduct': lastproduct,
               'toprated': toprated, 'trendproduct': trendproduct, 'bestseller': bestseller, 'productgrid': productgrid,'katagoriyarandom':katagoriyarandom} )


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesaj basariyla iletildi")
            return HttpResponseRedirect('/iletisim')
        else:
            messages.error(request,"Mesaj iletilemedi")

    setting = Settings.objects.get()
    form = ContactFormu()
    category = Category.objects.all()

    return render(request, 'pages/iletisim.html', context = {
        'setting': setting,
        'form': form,
        'category': category,
    })


def hakkimizda(request):
    setting = Settings.objects.get()
    category = Category.objects.all()
    return render(request, 'pages/hakkimizda.html', context = {
        'setting': setting,
        'category': category
    })



def referanslar(request):
    setting = Settings.objects.get()
    category = Category.objects.all()

    return render(request, 'pages/referanslar.html', context = {
        'setting': setting,
        'category': category
    })


def category_products(request, id, slug):
    setting=Settings.objects.get()
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    categorydata = Category.objects.get(pk=id)
    context = {'products': products, 'category': category, 'categorydata': categorydata,'setting':setting}
    return render(request, 'pages/products-grid.html', context)


def product_detail(request, id, slug):
    products=Product.objects.filter(category_id=id).order_by('?')[:4]
    setting=Settings.objects.get()
    category = Category.objects.all()
    product=Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    comments=Comment.objects.filter(product_id=id,status='True')
    return render(request, 'pages/product_detail.html', context={
        'category': category,
        'product':product,
        'images':images,
        'comments':comments,
        'setting':setting,
        'products':products

    })

def product_search(request):
    if request.method =='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            setting=Settings.objects.get()
            category=Category.objects.all()
            query=form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context={
                'products':products,
                'category':category,
                'setting' : setting,

            }
            return render(request,'pages/products_search.html',context)

    return HttpResponseRedirect('/')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           messages.success(request, "Uğurla hesabınıza daxil oldunuz ..")
           return HttpResponseRedirect('/')

       else:
           messages.error(request,"Giriş Xətası  | İstifadəçi adı və ya parol səhvdir! ")
           return HttpResponseRedirect('/login')



    setting=Settings.objects.get()
    return render(request,'pages/login_page.html',context={
        'setting' :setting
    })


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.jpg"
            data.save()
            messages.success(request, "Uğurla qeydiyyatdan keçdiniz ..")



            return HttpResponseRedirect('/')


    else:

        form = SignUpForm()
        messages.error(request, "Qeydiyyatda xəta baş verdi. Yenidən yoxlayın ..")

    setting=Settings.objects.get()
    return render(request,'pages/signup_page.html',context={
        'setting' :setting,
        'form': form
    })


