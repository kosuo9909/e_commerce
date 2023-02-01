from django.contrib.auth.decorators import login_required
from django.urls import path

# from accounts.forms import MyAuthForm
from accounts.views import LoginUser, RegisterUser, SignOut, ProfileView

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', login_required(SignOut.as_view()), name='logout'),
    path('profile/<int:pk>', login_required(ProfileView.as_view()), name='profile'),
]
