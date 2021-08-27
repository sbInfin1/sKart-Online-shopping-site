from .models import *
import json
import datetime
from django.contrib.auth.models import User

# This is not a view; the request is passed in so that we can access various values
# associated with request like .COOKIES etc.
def cookieCart(request):
    # In case the 'cart' cookie is not created yet (on first load the page),
    # we create a dummy dictionary to avoid error
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems':cartItems, 'order':order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        # customer = request.user.customer
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        get_cart_items = order.get_cart_items
        get_cart_total = order.get_cart_total
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']
        get_cart_items = order['get_cart_items']
        get_cart_total = order['get_cart_total']
        cartItems = cookieData['cartItems']
    return {'cartItems':cartItems, 'get_cart_items':get_cart_items, 
            'get_cart_total':get_cart_total, 'items':items}

def guestOrder(request, data):
    print("User is not Logged In")
    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    # This needs to be changed to the instantiation of the User class
    customer, created = User.objects.get_or_create(
        email=email,
    )
    customer.username = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
