from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Product(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=60,
    )

    price = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    old_price = models.PositiveIntegerField(blank=True, null=True)

    description = models.CharField(
        blank=True,
        null=True,
        max_length=120,
    )

    image = models.ImageField(
        default='defaults/default_product.png',
        blank=True,
        null=True,
        verbose_name='Product Photos',
    )

    on_sale = models.BooleanField(default=False)

    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.price} USD'


class ShoppingCart(models.Model):

    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)