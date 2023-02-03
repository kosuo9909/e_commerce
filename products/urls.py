from django.urls import path

from products.views import show_products

urlpatterns = [
    path('', show_products, name='products'),
]