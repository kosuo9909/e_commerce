from django.urls import path

from core.views import contacts

urlpatterns = [
    path('contacts/', contacts, name='contact'),
]