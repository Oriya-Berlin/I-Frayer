import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final_Project.settings')
django.setup()


import gzip
import xmltodict
import urllib.request
from django.shortcuts import render, redirect, reverse
from App.forms import LoginForm, RegisterForm, CalculateFormRL, CalculateFormVIC, CalculateFormY
from App.models import User, Item
from django.contrib import messages
from django.db.models import Q
from .functions import *


#
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            if User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.warning(request, f"{form.cleaned_data['email']} is already in exists")
                return redirect(reverse('register'))

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       gender=gender,
                                       date_of_birth=date_of_birth,
                                       age=calculateAge(date_of_birth),
                                       email=email,
                                       password=generateHash(password))
            if user:
                messages.success(request, 'Signup successful')
                return redirect(reverse('login_user'))
            else:
                messages.error(request, "Ohh Shit, something went wrong")
    else:
        form = RegisterForm()

    return render(request, 'Register.html', {'form': form})


#
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_pass = generateHash(password)

            if User.objects.get(Q(email=email), Q(password=hashed_pass)):  # we need to handle the exception
                user = User.objects.get(email=email)

                #if hashed_pass == user.get_pass():
                #login(request, user)
                messages.success(request, 'You are logged in')
                return redirect(reverse('products'))
            else:
                messages.error(request, 'Bad authentication')
                return redirect(reverse('login_user'))
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})


#
def add_product(request, product_id):
    item = Item.objects.get(id=product_id)
    items = request.session.get('cart', [])
    items.append(item.id)
    request.session['cart'] = items
    return redirect('products', item.Category)


#
def cart(request):
    items = [Item.objects.get(id=item) for item in request.session['cart']]
    num = len(items)

    if num == None:
        num = 0
    request.session['num'] = num   # define

    sum1 = 0
    sum2 = 0
    sum3 = 0

    if request.method == 'POST':
        form1 = CalculateFormRL(request.POST)
        form2 = CalculateFormVIC(request.POST)
        form3 = CalculateFormY(request.POST)

        sum1 = calculate_cart1('/home/berlin/Desktop/rami.xml', items)
        sum2 = calculate_cart2('/home/berlin/Desktop/vik.xml', items)
        sum3 = calculate_cart1('/home/berlin/Desktop/yohanan.xml', items)
    else:
        form1 = CalculateFormRL()
        form2 = CalculateFormVIC()
        form3 = CalculateFormY()
    return render(request, 'Cart.html', {'items': items, 'form1': form1, 'form2': form2, 'form3': form3, 'num': num, 'sum1': sum1, 'sum2': sum2, 'sum3': sum3})


#
def products(request, category='Milk'):
    num = request.session.get('num')  # call
    products_list = Item.objects.filter(Category=category)
    return render(request, 'Products.html', {'products': products_list, 'num': num})


#
def search(request):
    search_line = request.POST['search_line']
    result = Item.objects.filter(Item_Name__icontains=search_line).exclude(Image='')  # need to finish that
    return render(request, 'Products.html', {'products': result})


#
def entry(request):
    return render(request, 'Entry.html')

