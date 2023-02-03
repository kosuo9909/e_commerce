from django.shortcuts import render

from products.models import Product


def show_products(request):
    all_products = Product.objects.all()

    context = {
        'products': all_products,
    }

    return render(request, template_name='products/products.html', context=context)