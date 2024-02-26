from django.db import models
from django.utils import timezone

from computer_store.user.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="images", null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=15, null=False, blank=False)
    overview = models.CharField(max_length=1000, null=False, blank=False)
    description = models.CharField(max_length=10000, null=False, blank=False)
    sold = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="predator/image/", null=True, blank=True, default=None
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    delivery_to = models.CharField(max_length=255, null=False, blank=False)
    note = models.CharField(max_length=1000, null=True, blank=True)
    status = models.IntegerField(default=0)
    feedback = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id


class OrderItem(models.Model):
    order: models.ForeignKey(Order, on_delete=models.CASCADE)
    product: models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity: models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id
