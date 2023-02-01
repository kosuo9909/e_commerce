from django.urls import path

from core.views import contacts, about_us

urlpatterns = [
    path('contacts/', contacts, name='contact'),
    path('about/', about_us, name='about'),
]