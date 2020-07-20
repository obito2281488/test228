from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    price = models.FloatField()
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    main_image = models.ImageField(upload_to='media/product/')
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    product_amount = models.IntegerField(default=1)