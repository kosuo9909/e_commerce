from django.shortcuts import render

from accounts.models import CustomUserModel
from products.models import Product, ShoppingCart


def show_products(request):
    all_products = Product.objects.all()
    context = {
        'products': all_products,
    }

    return render(request, template_name='products/products.html', context=context)


def add_to_cart(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    user = CustomUserModel.objects.get(pk=request.user.pk)
    to_cart = ShoppingCart.objects.create()
    to_cart.user.add(user)
    to_cart.product.add(product)
    to_cart.save()

    all_products = Product.objects.all()
    current_cart = ShoppingCart.objects.filter(user=user)
    print(f'SSSS {current_cart}')
    context = {
        'products': all_products,
        'cart': current_cart,
    }

    return render(request, template_name='products/products.html', context=context)
