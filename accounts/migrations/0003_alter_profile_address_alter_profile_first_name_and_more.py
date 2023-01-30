# Generated by Django 4.1.5 on 2023-01-30 18:07

import accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), accounts.validators.validate_letters], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), accounts.validators.validate_letters], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(4)], verbose_name='Postcode'),
        ),
    ]
