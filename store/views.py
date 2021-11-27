from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
import razorpay

from store.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .utils import cookieCart, cartData, guestOrder

# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'imgHeight':'200px'}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    items = data['items']
    get_cart_items = data['get_cart_items']
    get_cart_total = data['get_cart_total']
    cartItems = data['cartItems']

    context = {'items':items, 'get_cart_items':get_cart_items, 
                'get_cart_total':get_cart_total, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    items = data['items']
    cartItems = data['cartItems']
    get_cart_items = data['get_cart_items']
    get_cart_total = data['get_cart_total']
    total_amt_in_paise = get_cart_total * 100

    context = {'items':items, 'get_cart_items':get_cart_items, 
                'get_cart_total':get_cart_total, 'cartItems': cartItems, 
                'total_amt_in_paise': total_amt_in_paise}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action: {}, productId: {}'.format(action, productId))

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer = customer,
        order = order,
        address = data['shipping']['address'],
        city = data['shipping']['city'],
        zipcode = data['shipping']['zipcode'],
    )

    # Razorpay integration
    if request.method == 'POST':
        amount = total*100
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        client = razorpay.Client(auth=('rzp_test_czwexr0tNemZtI', '5T3SrkKGFdsZqeUWbBUS536a'))
        payment = client.order.create(amount=amount, currency=order_currency, receipt=order_receipt)

    return JsonResponse('Payment complete', safe=False)

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    menUpperProducts = Product.objects.filter(category='men_upper')

    menUpperProductsArr = []
    for i in range(0, len(menUpperProducts), 4):
        menUpperProductsArr.append(menUpperProducts[i:min(i+4, len(menUpperProducts))])

    womenWearProducts = Product.objects.filter(category='women_wear')

    womenWearProductsArr = []
    for i in range(0, len(womenWearProducts), 4):
        womenWearProductsArr.append(womenWearProducts[i:min(i+4, len(womenWearProducts))])


    context = {'products': products, 'menUpperProductsArr':menUpperProductsArr ,
        'womenWearProductsArr':womenWearProductsArr, 'cartItems': cartItems}
    return render(request, 'store/homepage.html', context)

def filteredStore(request, category = "all"):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.filter(category=category)

    imgHeight = '200px'
    if category == 'men_upper' or category == 'women_wear':
        imgHeight = '360px'
    elif category == 'headphones':
        imgHeight = '330px'
    elif category == 'gaming_laptop':
        imgHeight = '250px'

    context = {'products': products, 'cartItems': cartItems, 'imgHeight':imgHeight}
    return render(request, 'store/store.html', context)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            # Hashing the password using the set_password() method
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    context = {'user_form': user_form, 'registered': registered}
    return render(request, 'registration/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE.')
        else:
            print("Someone tried to login and failed.")
            print("Username {} and password: {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED.")
    else:
        return render(request, 'registration/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
