from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('', entry, name='Entry'),                  # TODO: problem

    path('products/<category>', products, name='products'),

    path('products/', products, name='products_default'),

    path('products/add/<int:product_id>', add_product, name='add_to_cart'),

    path('products/search/', search, name='search'),
    path('cart', cart, name='cart'),
]
