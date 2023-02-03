from django.shortcuts import render


# Create your views here.
def contacts(request):
    return render(request, template_name='core/contacts.html')


def about_us(request):
    return render(request, template_name='core/about.html')

