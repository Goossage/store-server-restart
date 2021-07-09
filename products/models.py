from django.db import models
from users.models import User
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to="products_images", blank = True)
    name = models.CharField(max_length=256, unique=True)
    short_description = models.CharField(max_length=256, blank = True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f' {self.name} | {self.category}'

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)