from rest_framework import serializers

from ..models import ShoppingCard, Product, ShoppingItem


class ShoppingCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCard
        fields = ('id', 'name', 'email', 'phone', 'address')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


