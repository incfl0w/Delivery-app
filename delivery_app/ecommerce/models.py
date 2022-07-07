from django.db import models


class ShoppingCard(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=124)
    price = models.FloatField(default=0)


class ShoppingItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    shopping_card = models.ForeignKey(ShoppingCard, on_delete=models.CASCADE)
