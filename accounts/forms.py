from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accounts.models import Profile

user_model = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = user_model
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class LoginForm(UserCreationForm):
    class Meta:
        model = user_model
        fields = ['username', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
