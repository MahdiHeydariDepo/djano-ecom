from django.db import models
import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/product/')
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=120, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product}"
