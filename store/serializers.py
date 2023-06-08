from dataclasses import fields
from decimal import Decimal
from itertools import product
from multiprocessing import managers
from pyexpat import model
from rest_framework import serializers
from store.models import Cart, CartItem, Collection, Product, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "featured_product", "products_count"]

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Product.objects.all(), view_name="collection-detail"
    # )

    def calc_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # override the creation of a new product
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.inventory += 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get("unit_price")
    #     instance.save()
    #     return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "unit_price",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name="get_total_price")

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price
    
    def create(self, validated_data):
        cart_id = self.context["cart_id"]
        return CartItem.objects.create(cart_id=cart_id, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name="get_total_price")

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, cart: Cart):
        return sum(item.product.unit_price*item.quantity for item in cart.items.all())
