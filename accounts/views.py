from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
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


@login_required
class SignOut(LogoutView):
    next_page = reverse_lazy('index')


@login_required
class ProfileView(UpdateView):
    template_name = 'profile-test.html'
    model = Profile

    fields = ('first_name', 'last_name', 'address', 'postcode')

    def form_valid(self, form):
        print(f'worked, here is the form {form}')
        return super(ProfileView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def form_invalid(self, form):
        print('ERRORRRRR')
        print(form)
        return super(ProfileView, self).form_invalid(form)
