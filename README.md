# sKart-Online-shopping-site
Django-based online shopping site

## Overview
`sKart` is a Django-based Ecommerce website like Amazon, Flipkart, etc. The website has a homepage where sale banners are displayed along with items for sale just like any typical ecommerce website. There is also a dedicated page for each product category. Each user visiting the website can either choose to register themselves and then login with their credentials or remain anonymous. `sKart` gives unanonymous users the facility to add items to the `cart` using browser cookies. Although anonymous users must register themselves before placing an order. In the `checkout` page, there is a Paypal payment option to pay for the items in the cart.

## Homepage
### Sale banner
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/homepage.JPG" width="1024" height="548" title="homepage"/>

### Men's shirt sale in homepage
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/mens_shirts_sale_homepage.JPG" width="1024" height="548" title="mens_shirts_sale_homepage"/>

## Navbar
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/womens_sale_homepage.JPG" width="1024" height="548" title="womens_sale_homepage"/>

The `Navbar` houses a few buttons the navigating between various pages of the website. The `Navbar Brand` button bearing the name `sKart` appears at left, upon clicking which the user is directed to the homepage from wherever they are currently. The `Store` button directs the user to the general store page where all the items in store are listed. The `Categories` drop-down menu lists all categories of items, and clicking any one of them directs the user to the `Store` page populated with items of that particular category. The search bar is non-functional. The `Register` button is used to create the record of a new customer whereas the `Login` button is used by a pre-registered user to log in to the website to purchase items. The Navbar also houses a `Cart` icon which displays the number of items currently in the cart.

## User Registration and Login
### Before signup or registration
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/new_user_signup.JPG" width="1024" height="548" title="new_user_signup"/>

### After signup
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/after_signup.JPG" width="1024" height="548" title="after_signup"/>

### Before Login
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/user_login.JPG" width="1024" height="548" title="user_login"/>

### After Login
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/after_login.JPG" width="1024" height="548" title="after_login"/>

Note that after logging in, the `Register` and `Login` buttons disappear. In place of that, we see a greeting message to the user.

## Store
### Headphone store page with no item added to cart yet
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/cart_empty.JPG" width="1024" height="548" title="cart_empty"/>

### One of the headphones added to the cart
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/headphone_added_to_cart.JPG" width="1024" height="548" title="headphone_added_to_cart"/>

Note that the cart icon now shows a `1`, which indicates that currently the cart holds one item.

## Cart
### Cart page with the headphone as the only item
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/view_cart.JPG" width="1024" height="548" title="view_cart"/>

From the `Cart` page, the customer can either choose to proceed to the `Checkout` page or click on the `continue Shopping` button to go back to the store page.

## Checkout
### Checkout page with the headphone as the only order item
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/checkout_page.JPG" width="1024" height="548" title="checkout_page"/>

### Payment options
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/razorpay_button.JPG" width="1024" height="548" title="checkout_page_payment"/>

On entering the name, email and shipping address details, the payment options get unlocked. The user can then, pay the required amount using `Razorpay` to complete the order.

<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/razorpay_window.JPG" width="1024" height="548" title="checkout_page_payment"/>
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/razorpay_payment.JPG" width="1024" height="548" title="checkout_page_payment"/>
<img src="https://github.com/sbInfin1/sKart-Online-shopping-site/blob/Moving_forward/screenshots/transaction_complete.JPG" width="1024" height="548" title="checkout_page_payment"/>

