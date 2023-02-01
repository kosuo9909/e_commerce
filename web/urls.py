from django.urls import path

import core.urls
from web import views

urlpatterns = [

    path('', views.index, name='index'),

]
