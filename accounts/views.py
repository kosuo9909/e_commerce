from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import RegisterForm
from accounts.models import Profile


class LoginUser(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        return super(LoginUser, self).form_valid(form)


class RegisterUser(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super(RegisterUser, self).form_valid(form)
        login(self.request, self.object)
        return valid


class SignOut(LogoutView):
    next_page = reverse_lazy('index')


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = Profile
