from django.urls import path

# from accounts.forms import MyAuthForm
from accounts.views import LoginUser, RegisterUser, SignOut

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', SignOut.as_view(), name='logout'),
]
