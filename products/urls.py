from django.urls import path

from products.views import show_products, add_to_cart, show_cart, remove_from_cart, show_on_sale

urlpatterns = [
    path('', show_products, name='products'),
    path('add/<int:product_pk>', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_pk>', remove_from_cart, name='remove from cart'),
    path('cart/', show_cart, name='show cart'),
    path('sale/', show_on_sale, name='show sale'),
]