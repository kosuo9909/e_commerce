from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import RegisterForm, ProfileForm
from accounts.models import Profile, CustomUserModel


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


class ProfileView(UpdateView):
    template_name = 'profile-test.html'
    model = Profile

    fields = ('first_name', 'last_name', 'address', 'postcode')


class UpdateProfile(DetailView):
    template_name = 'profile.html'
    model = Profile

    fields = ('first_name', 'last_name', 'age', 'profileimg', 'location')
