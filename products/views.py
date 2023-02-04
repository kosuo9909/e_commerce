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
    to_cart = ShoppingCart.objects.create(
        user=user,
        product=product,
    )
    to_cart.save()
    all_products = Product.objects.all()
    current_cart = ShoppingCart.objects.filter(user=user)
    print(f'SSSS {current_cart}')
    context = {
        'products': all_products,
        'cart': current_cart,
    }

    return render(request, template_name='products/products.html', context=context)


def show_cart(request):
    current_cart = ShoppingCart.objects.filter(user=request.user)
    total_price = [int(x.product.price) for x in current_cart]
    summed_price= sum(total_price)
    context = {
        'cart': current_cart,
        'amount': summed_price,
    }
    return render(request, template_name='products/shopping_cart.html', context=context)


def remove_from_cart(request, product_pk):
    item = None

    try:
        product = Product.objects.get(pk=product_pk)
        item = ShoppingCart.objects.filter(product=product, user=request.user)
    except:
        pass

    if item:
        item.delete()

    current_cart = ShoppingCart.objects.filter(user=request.user)
    total_price = [int(x.product.price) for x in current_cart]
    summed_price = sum(total_price)
    context = {
        'cart': current_cart,
        'amount': summed_price,
    }
    return render(request, template_name='products/shopping_cart.html', context=context)