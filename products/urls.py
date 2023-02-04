from django.urls import path

from products.views import show_products, add_to_cart

urlpatterns = [
    path('', show_products, name='products'),
    path('add/<int:product_pk>', add_to_cart, name='add_to_cart'),
]