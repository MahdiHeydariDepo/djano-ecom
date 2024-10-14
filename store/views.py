from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from store.models import Product, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.template.defaultfilters import slugify


# Create your views here.
def category(request, foo):
    foo = foo.replace("-", " ")
    categories = Category.objects.all()
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',
                      {'category': category, 'products': products, 'categories': categories} )
    except:
            messages.success(request, 'THIS CATEGORY IS NOT AVAILABLE')
            return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html',
                  {'categories': categories})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products
                                         , 'categories': categories})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Are Now Logged In')
            return redirect('home')

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out! ')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you are registered successfully!')
            return redirect('home')
        else:
            messages.error(request, 'please try again, there was an error')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
