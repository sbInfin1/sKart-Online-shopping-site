from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name = 'store'),
    path('store/<slug:category>/', views.filteredStore, name='filteredStore'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]
