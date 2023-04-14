from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


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
