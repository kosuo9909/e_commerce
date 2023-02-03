from django.db import models


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

    description = models.CharField(
        blank=True,
        null=True,
        max_length=120,
    )

    image = models.ImageField(
        default='defaults/default_product.png',
        upload_to='product_photos',
        blank=True,
        null=True,
        verbose_name='Product Photos',
    )

    def __str__(self):
        return f'{self.name} - {self.price} USD'
