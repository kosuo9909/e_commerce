# Generated by Django 4.1.5 on 2023-02-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, default='defaults/default_product.png', null=True, upload_to='product_photos', verbose_name='Product Photos')),
            ],
        ),
    ]