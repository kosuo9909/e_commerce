# Generated by Django 4.1.5 on 2023-02-03 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_profile_shopping_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusermodel',
            name='shopping_cart',
        ),
    ]
