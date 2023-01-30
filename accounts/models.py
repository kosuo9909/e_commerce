from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from accounts.managers import CustomUserManager
from accounts.validators import validate_letters


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name_plural = 'Users'

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    username = models.CharField(
        unique=True,
        max_length=30,
        validators=(
            validators.MinLengthValidator(4),
            validate_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Profiles'

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(2),
            validate_letters,
        )
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_letters,
        )
    )

    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, primary_key=True, )

    address = models.CharField(
        max_length=200,
        blank=True,
    )

    postcode = models.IntegerField(
        blank=True,
        default=0000,
        validators=[
            validators.MinValueValidator(4),
        ]
    )

    def __str__(self):
        return self.first_name + self.last_name


@receiver(post_save, sender=CustomUserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
