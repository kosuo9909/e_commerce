from django.shortcuts import render


def show_products(request):
    return render(request, template_name='products/products.html')